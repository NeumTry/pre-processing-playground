import streamlit as st

from PreprocessingPlayground.preprocessing import preprocessing
from EmbedddingsPlayground.embeddings import embeddings

if "page" not in st.session_state:
    st.session_state["page"] = "preprocessing"
if "dbs" not in st.session_state:
    st.session_state["dbs"] = []
if "results" not in st.session_state:
    st.session_state["results"] = []
if "choices" not in st.session_state:
    st.session_state["choices"] = ["","",""]

with st.sidebar:
    st.title("Neum AI Playground")
    st.markdown("Neum AI helps you connect and synchronize your data to a vector database. Simply set up a pipeline and let Neum AI automatically synchronize your data.")
    st.markdown("This app allows you to test different embedding configuration across models, queries and chunks.")

    if st.button("Test input preprocessing"):
        st.session_state.page = "chunks_query"
    if st.button("Test embeddings models"):
        st.session_state.page = "embeddings"

if st.session_state.page == "preprocessing":
    preprocessing()

if st.session_state.page == "embeddings":
    embeddings()