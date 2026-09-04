# AI Assistant - Task 1 (Local Setup)

## Overview
A local Retrieval-Augmented Generation (RAG) assistant leveraging Llama 3.1 via Ollama, ChromaDB, tool binding, and structured JSON outputs.

## Features
- **Local Model**: Llama 3.1 served natively via Ollama
- **Vector DB**: ChromaDB with Ollama embeddings
- **Schema Validation**: Pydantic structured output
- **Tools**: Dynamic function integration with LangChain

## 🏗️ Architecture & System Design

+-----------------------------------------------------------------------------------+
|                                 USER INPUT QUERY                                  |
|                  ("What vector database is used in this system?")                 |
+-----------------------------------------------------------------------------------+
|
v
+-----------------------------------------------------------------------------------+
|                            PROMPT & CONTEXT HANDLING                              |
|           (Ingestion via Document Loader & Recursive Chunking Engine)             |
+-----------------------------------------------------------------------------------+
|
+----------------------+----------------------+
|                                             |
v                                             v
+------------------------------------+        +------------------------------------+
|            RAG PIPELINE            |        |           TOOL CALLING             |
|  - Text Ingestion & Chunking       |        |  - Dynamic Python Functions        |
|  - ChromaDB Vector Store           |        |  - System Uptime Calculators       |
|  - Ollama Dense Embeddings         |        |  - Tool Binding Engine             |
+------------------------------------+        +------------------------------------+
|                                             |
+----------------------+----------------------+
|
v
+-----------------------------------------------------------------------------------+
|                                LOCAL LLM INFERENCE                                |
|                         Llama 3.1:8b (Served via Ollama)                          |
+-----------------------------------------------------------------------------------+
|
v
+-----------------------------------------------------------------------------------+
|                              STRUCTURED OUTPUT LAYER                              |
|                   Pydantic Schema Validation (Strict JSON Format)                 |
+-----------------------------------------------------------------------------------+

## How to Run locally

1. Ensure Ollama is running on your machine:
   ```bash
   ollama serve

2. Run the application:
   ```bash
   python app.py
