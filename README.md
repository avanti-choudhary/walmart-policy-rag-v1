# wal# Walmart Policy RAG - V1 (Prototype - Legacy)

> **Status:** Prototype built with Junior Vibe Coding Loop
> **Goal:** Test if RAG can answer Walmart policy questions

### Problem
Walmart employees waste 30+ mins searching 100+ policy PDFs.

### Architecture V1
Streamlit -> Titan Embeddings -> ChromaDB (Local) -> Claude 3.5 -> Answer

### What I Built
- Working Streamlit app with 10 PDFs
- Basic RAG pipeline

### Limitations (Why V2 was needed)
- ChromaDB = local only, no scaling, crashes at 100+ docs
- No Redis Cache = slow 3s for same question
- No Reranking = accuracy only 71%
- No SQS = upload blocks UI
- No evaluation metrics

### Learnings -> V2
Migrated to: Postgres pgvector + Redis Cache + Cohere Reranker (89% accuracy) + SQS + FastAPI + ECS Fargate

### Production Version
👉 [V2 Repo - Production Ready](https://github.com/avanti-choudhary/walmart-policy-rag-v2)

*V1 shows where I started, V2 shows production thinking.*mart-policy-rag-v1
