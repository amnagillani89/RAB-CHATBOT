from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# load CV
with open("cv.txt", "r", encoding="utf-8") as f:
    text = f.read()

# split text
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
docs = splitter.create_documents([text])

# embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# create FAISS index
db = FAISS.from_documents(docs, embeddings)

# save it
db.save_local("faiss_index")

print("FAISS CREATED")