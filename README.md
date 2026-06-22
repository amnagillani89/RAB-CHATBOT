# 🤖 AmanBot – Personal RAG-Based Chatbot

## 👤 Project Overview
AmanBot is a Retrieval-Augmented Generation (RAG) based chatbot built using Python and Streamlit.  
It is designed to answer questions based on a custom personal dataset (Aman Naveed’s CV).

The system retrieves relevant information using FAISS and generates contextual responses using embeddings and (optional) LLM integration.

---

## 🎯 Features
- Personal chatbot identity (AmanBot)
- Answers based only on custom CV dataset
- RAG-based architecture (Retrieval + Generation)
- Semantic search using embeddings
- FAISS vector database for fast retrieval
- Streamlit web-based chatbot interface
- Chat-style interaction

---

## 🧠 How It Works (RAG Pipeline)

User Query → Embedding → FAISS Search → Relevant Context → Response Generation → Final Answer

Steps:
1. User enters a question
2. Query is converted into vector embeddings
3. FAISS finds the most relevant CV chunks
4. Retrieved context is passed to response generator
5. System returns a contextual answer

---

## 🛠️ Technologies Used
- Python
- Streamlit (UI)
- FAISS (Vector Database)
- Sentence-Transformers (Embeddings)
- HuggingFace Transformers (optional LLM)
- NLP (Natural Language Processing)

---

## 📂 Dataset
Custom personal dataset including:

- CV (Aman Naveed)
- Education details
- Skills (Python, C++, Java)
- Academic projects
- Interests and profile information

Data is chunked and converted into embeddings for retrieval.

---

## ⚙️ System Architecture
- Document Loading
- Text Preprocessing
- Chunking
- Embedding Generation
- FAISS Indexing
- Similarity Search
- Response Generation
- Streamlit UI

---

## ▶️ How to Run the Project

### 1. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
Open in browser

After running, open:

http://localhost:8501
