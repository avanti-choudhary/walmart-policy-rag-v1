import streamlit as st
from rag import get_answer

st.set_page_config(page_title="Walmart Policy RAG V1", layout="centered")

st.title("Walmart Policy RAG - V1")
st.caption("Prototype - Streamlit + Chroma + Titan + Claude")

question = st.text_input("Ask about Walmart policy:", placeholder="What is dress code policy?")

if st.button("Get Answer") and question:
    with st.spinner("Searching policy docs..."):
        answer, sources = get_answer(question)
        st.subheader("Answer:")
        st.write(answer)
        st.subheader("Sources:")
        for src in sources:
            st.write(f"- {src}")

st.divider()
st.info("V1 Limitations: Local ChromaDB only, No Cache, No Reranking -> See V2 for production fix")
