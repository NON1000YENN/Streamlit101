import streamlit as st
st.set_page_config(page_title="CAD File Uploader Example", page_icon=":rocket:", layout="wide",)
st.title("CAD File Uploader Examplepage")

st.write("Import file uploader")
st.file_uploader("Upload a file", type=["json"])
