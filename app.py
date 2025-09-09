from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.promt import *
import os

# Khởi tạo Flask
app = Flask(__name__)

# Load biến môi trường
load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Load embeddings
embeddings = download_hugging_face_embeddings()

# Kết nối Pinecone
index_name = "medicalbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

# Tạo retriever
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Khởi tạo LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.4,
    api_key=OPENAI_API_KEY   # dùng key từ env
)

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

# Tạo chain
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Routes
@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]  # ✅ sửa cách lấy dữ liệu
    print("User:", msg)

    response = rag_chain.invoke({"input": msg})
    print("Response:", response["answer"])

    return str(response["answer"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
