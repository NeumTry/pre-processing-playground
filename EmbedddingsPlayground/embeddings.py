from typing import List
import streamlit as st
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def embeddings():
    st.title("Test embedding models")
    st.caption("Embed using multiple embeddings models on a set of chunks against a query.")

    st.subheader("Choose embed models")
    models = ["text-ada-002","bge-small-en","mpnet-v2"]
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.session_state.choices[0] = st.selectbox("model", models, key="choice1")
    with col2:
        st.session_state.choices[1] = st.selectbox("model", models, key="choice2")
    with col3:
        st.session_state.choices[2] = st.selectbox("model", models, key="choice3")

    st.subheader("Add chunks")
    chunks = st.text_area("Chunks", height=300)
    st.caption("Copy/Paste chunks separated by `---------------------------`")
    if st.button("Embed Chunks", use_container_width=True):
        st.session_state.dbs = []
        separated_chunks = processChunks(chunks)
        for model in st.session_state.choices:
            if model == "text-ada-002":
                embeddings = EmbeddingsOpenAI()
            elif model == "bge-small-end":
                embeddings = EmbeddingsBGE()
            elif model == "mpnet-v2":
                embeddings = EmbeddingsMpnet()
            db = Chroma.from_texts(texts=separated_chunks, embedding=embeddings)
            st.session_state.dbs.append(db)
    
    st.subheader("Query chunks")
    query = st.text_input("Query")
    if st.button("Query Chunks", use_container_width=True):
        st.session_state.results = []
        for db in st.session_state.dbs:
            result = db.similarity_search_with_score(query, 3)
            st.session_state.results.append(result)
    if len(st.session_state.results) >  0:
        st.subheader("Results")
        choice1, choice2, choice3 = st.columns([1,1,1])
        with choice1:
            st.text(st.session_state.choices[0])
            for r in st.session_state.results[0]:
                docs, similarity = r
                st.markdown(docs.page_content)
                st.text("Similarity: " + str(similarity))
                st.divider()
        with choice2:
            st.text(st.session_state.choices[1])
            for r in st.session_state.results[1]:
                docs, similarity = r
                st.markdown(docs.page_content)
                st.text("Similarity: " + str(similarity))
                st.divider()
        with choice3:
            st.text(st.session_state.choices[2])
            for r in st.session_state.results[2]:
                docs, similarity = r
                st.markdown(docs.page_content)
                st.text("Similarity: " + str(similarity))
                st.divider()

def EmbeddingsOpenAI():
    return OpenAIEmbeddings()

def EmbeddingsBGE():
    model_name = "BAAI/bge-small-en"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

def EmbeddingsMpnet():
    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

def processChunks(chunks:str):
    return [part.strip() for part in chunks.split('---------------------------') if part.strip() != '']
