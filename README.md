# AI Assistant - Task 1 (Local Setup)

## Overview
A local Retrieval-Augmented Generation (RAG) assistant leveraging Llama 3.1 via Ollama, ChromaDB, tool binding, and structured JSON outputs.

## Features
- **Local Model**: Llama 3.1 served natively via Ollama
- **Vector DB**: ChromaDB with Ollama embeddings
- **Schema Validation**: Pydantic structured output
- **Tools**: Dynamic function integration with LangChain

## Architecture

+------------------+      +-------------------+      +-------------------+
|  User Query /    | ---> | RAG Vector Store  | ---> |   Ollama Engine   |
| System Prompt    |      |    (ChromaDB)     |      |  (Llama 3.1:8b)   |
+------------------+      +-------------------+      +-------------------+
|                                                    |
v                                                    v
+------------------+                                 +-------------------+
|   Tool Calling   | -------------------------------> | Validated JSON    |
|   (Python Exec)  |                                 | Response (Schema) |
+------------------+                                 +-------------------+

## How to Run locally

1. Ensure Ollama is running on your machine:
   ```bash
   ollama serve

2. Run the application:
   ```bash
   python app.py
