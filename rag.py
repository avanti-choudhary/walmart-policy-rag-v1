import chromadb

# V1 Simple Setup - Local ChromaDB
# Note: In real V1, we used Titan Embeddings + Claude via Bedrock
# For GitHub demo, using dummy logic so code runs

client = chromadb.Client()
collection = client.get_or_create_collection("walmart_policies")

def get_answer(question: str):
    # V1 Logic: Query Chroma -> Send to Claude -> Return
    # Placeholder for demo - In real app, this calls Bedrock

    # Simulating retrieval
    results = collection.query(query_texts=[question], n_results=3)

    # Simulating Claude response
    answer = f"Based on policy docs, answer for '{question}' is: [This is V1 prototype response. V2 has 89% accuracy with Reranker]"
    sources = ["Policy_HR_001.pdf - Page 12", "Policy_DressCode_2024.pdf"]

    return answer, sources

def add_document(text, doc_id):
    collection.add(documents=[text], ids=[doc_id])
