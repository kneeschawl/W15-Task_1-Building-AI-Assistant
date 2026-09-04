import json
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.tools import tool
from pydantic import BaseModel, Field

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# --- 1. RAG PIPELINE: INGESTION & CHUNKING ---
sample_doc_content = """
The AI Assistant system is built with a hybrid approach:
- Local LLM: Llama 3.1 8B served via Ollama for privacy and offline tasks.
- Vector Database: ChromaDB for storing and retrieving document embeddings.
- RAG Architecture: Augments LLM responses using semantic search over knowledge bases.
- Tool Integration: Executes dynamic python functions to compute system metrics.
"""

with open("knowledge_base.txt", "w") as f:
    f.write(sample_doc_content)

loader = TextLoader("knowledge_base.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=20)
chunks = text_splitter.split_documents(documents)

# --- 2. VECTORIZATION & RETRIEVAL ---
print("Initializing ChromaDB & Local Embeddings...")
embeddings = OllamaEmbeddings(model="llama3.1:8b")
vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# Retrieve relevant context
query = "What vector database is used?"
retrieved_docs = retriever.invoke(query)
retrieved_context = retrieved_docs[0].page_content

# --- 3. TOOLS & STRUCTURED OUTPUT ---
@tool
def calculate_system_uptime(days_active: int) -> str:
    """Calculates operational uptime percentage based on days active."""
    total_hours = days_active * 24
    return f"System active for {total_hours} total hours with 99.9% uptime."

class AssistantResponse(BaseModel):
    summary: str = Field(description="Direct concise answer to the query.")
    confidence_score: float = Field(description="Confidence rating between 0.0 and 1.0.")
    retrieved_sources: list[str] = Field(description="Context pieces used.")

# --- 4. MODEL INITIALIZATION & EXECUTION ---
print("Connecting to local Llama 3.1...")
llm = ChatOllama(model="llama3.1:8b", temperature=0.2)
llm_structured = llm.with_structured_output(AssistantResponse)

prompt = f"Context: {retrieved_context}\nQuestion: {query}"
response = llm_structured.invoke(prompt)

print("\n--- Validated JSON Response ---")
print(json.dumps(response.model_dump(), indent=2))