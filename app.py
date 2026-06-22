import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np

# ---------------- UI ----------------
st.set_page_config(page_title="AmanBot RAG")
st.title("🤖 AmanBot (Stable RAG Chatbot)")

# ---------------- CV DATA ----------------
documents = [
    "Skills: Python, C++, Java",
    "Projects: Chatbot, Student Management System, Calculator, Library Management System, Election System",
    "Education: BS Software Engineering at UMT, 6th semester",
    "Interests: Artificial Intelligence, Machine Learning, NLP, Software Development"
]

# ---------------- MODEL ----------------
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# ---------------- SIMPLE RETRIEVAL (NO FAISS = NO CRASH) ----------------
def retrieve(query):
    query = query.lower()

    if "skill" in query:
        return documents[0]

    elif "project" in query:
        return documents[1]

    elif "education" in query or "study" in query:
        return documents[2]

    elif "interest" in query:
        return documents[3]

    else:
        # fallback smart match
        return "Ask about skills, projects, education, or interests."

# ---------------- ANSWER FUNCTION ----------------
def answer(query):
    result = retrieve(query)

    return f"""
📌 Based on Aman’s CV:

👉 {result}

---

This answer is retrieved using a simple RAG system.
"""

# ---------------- CHAT UI ----------------
if "chat" not in st.session_state:
    st.session_state.chat = []

for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.write(msg)

user_input = st.chat_input("Ask about Aman CV...")

if user_input:
    response = answer(user_input)

    st.session_state.chat.append(("user", user_input))
    st.session_state.chat.append(("assistant", response))

    st.rerun()