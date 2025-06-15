import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from qdrant_client import QdrantClient
import os

# -------------------- Setup -------------------- #

st.set_page_config(page_title="Tech Education & Hiring Market Trends", layout="wide")
st.title("📰 Tech Education & Hiring Market Trends")

# Load environment variables
load_dotenv()
hf_token = os.getenv("hf_token")
qdrant_token = os.getenv("qdrant_token")

# Constants
COLLECTION_NAME = "news_articles"
EMBEDDING_MODEL = "intfloat/multilingual-e5-large"

# Clients
embedding_client = InferenceClient(api_key=hf_token)
llm_client = InferenceClient(api_key=hf_token, provider="cerebras")

vector_db_client = QdrantClient(
    url="https://cf58605f-3b88-494f-9b09-dcc67ca3478b.europe-west3-0.gcp.cloud.qdrant.io:6333",  # from Qdrant Cloud
    api_key=qdrant_token
)

# -------------------- User Query -------------------- #

query = st.chat_input("find relationship between tech labour market trends and guidlines for educators")

if query:
    with st.spinner("🔎 Searching articles..."):

        # Step 1: Embed query
        embedding = embedding_client.feature_extraction(
            query,
            model=EMBEDDING_MODEL,
        )

        # Step 2: Search similar articles
        results = vector_db_client.search(
            collection_name=COLLECTION_NAME,
            query_vector=embedding,
            limit=4,
            with_payload=True
        )

        # Step 3: Format for context
        document_blocks = []
        for i, hit in enumerate(results):
            title = hit.payload.get("title", "Untitled")
            url = hit.payload.get("url", "")
            chunk = hit.payload.get("chunk", "")

            block = f"--- Article {i+1}: {title} ---\nURL: {url}\n\n{chunk}\n"
            document_blocks.append(block)

        context = "\n\n".join(document_blocks)

        # Step 4: Prompt LLM
        full_prompt = (
            f"User question:\n\"{query}\"\n\n"
            f"Here are some relevant excerpts from news articles:\n\n"
            f"{context}\n\n"
            f"Based on the articles, please answer the user's question clearly and cite relevant snippets if possible."
        )

        response = llm_client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct",
            messages=[{"role": "user", "content": full_prompt}]
        )

        answer = response.choices[0].message.content

    # -------------------- Display Output -------------------- #

    st.subheader("💬 Your Question")
    st.markdown(f"> {query}")

    st.subheader("📄 Relevant Articles")
    for i, hit in enumerate(results):
        st.markdown(f"**{hit.payload.get('title', 'Untitled')}**")
        st.markdown(f"[🔗 Read more]({hit.payload.get('url', '')})")
        with st.expander(f"Snippet {i+1}"):
            st.write(hit.payload.get("chunk", ""))

    st.subheader("🤖 AI Answer")
    st.markdown(answer)
