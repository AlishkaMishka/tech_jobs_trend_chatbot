# tech_jobs_trend_chatbot
This is a chatbot that uses news articles text on latest tech jobs trends to help entry role seekers as well as tech educators, that prepare students and professionals to work in tech.
# 📰 AI-Powered News Chatbot for Tech Hiring Trends

A conversational AI app that lets users ask questions about the latest **AI, data science, and tech hiring trends**—powered by **Google search**, **article scraping**, **semantic embeddings**, **vector search (Qdrant)**, and **LLM-based Q&A (LLaMA 3 via Hugging Face)**.

---

## 🚀 Features

- 🔍 **Automated article discovery** using advanced keyword queries on Google.
- 🧠 **Semantic chunking & embeddings** using Hugging Face's `intfloat/multilingual-e5-large`.
- 💾 **Vector storage & retrieval** with Qdrant Cloud for scalable search.
- 🤖 **LLM-based answers** using Meta’s LLaMA 3.3B-70B via Hugging Face Inference API.
- 💬 **Interactive chatbot interface** with Streamlit.

---

## 🎯 Project Goals

- Help beginners and career switchers navigate **entry-level AI/data science careers**.
- Track and summarize **education programs**, **hiring practices**, and **curriculum changes**.
- Provide a user-friendly Q&A interface for **insightful news-based answers**.

---

## 🛠️ Tech Stack

| Component         | Tool/Library                             |
|------------------|-------------------------------------------|
| Web UI           | Streamlit                                 |
| Search Engine    | Google Search (`googlesearch`)            |
| Article Scraper  | `newspaper3k`                             |
| Embeddings       | Hugging Face (`intfloat/multilingual-e5-large`) |
| Vector Database  | Qdrant Cloud                              |
| Language Model   | Meta LLaMA 3 (via Hugging Face Inference API) |
| Environment Vars | `python-dotenv`                           |

---

## 📁 Project Structure

```bash
📂 /notebooks/
    - article_scraper.ipynb          # Fetch articles using Google + Newspaper3k
    - embed_and_upload.ipynb         # Create vector embeddings and upload to Qdrant
📄 streamlit_app.py                  # Main chatbot interface
📝 .env                              # API keys (HF & Qdrant)
📄 tech_trends_news.csv              # Collected article data

🧪 How to Run
1. Setup
bash
Copy
Edit
git clone https://github.com/your-username/news-chatbot.git
cd news-chatbot
pip install -r requirements.txt
2. Environment Variables
Create a .env file:

ini
Copy
Edit
hf_token=your_huggingface_api_key
qdrant_token=your_qdrant_api_key
3. Collect Articles
Use the notebook or script to fetch and save articles to tech_trends_news.csv.

4. Embed & Upload to Qdrant
Run your notebook to embed articles and push them to your Qdrant collection (news_articles).

5. Launch the Chatbot
bash
Copy
Edit
streamlit run streamlit_app.py
🌐 Deployment
Local: Open http://localhost:8501

LAN: Share via your local IP address

Public: Use Streamlit Community Cloud or services like Hugging Face Spaces for external access.

🙋‍♂️ Who It's For
🧑‍🎓 Aspiring data scientists

🧑‍🏫 Educators designing modern AI/ML curricula

💼 Recruiters interested in tech hiring signals

📰 Researchers tracking education & employment trends

📌 Future Improvements
✅ Chat history

🔄 Daily auto-refresh from Google

🌍 Multilingual support

🧩 Plugin/embed options for career portals or LMS

📄 License
MIT License

🤝 Acknowledgments
Hugging Face 🤗 for inference and embeddings

Qdrant for lightning-fast vector search

Streamlit for the chat UI
