import streamlit as st

# ต้องอยู่บนสุดสุด ก่อนคำสั่ง Streamlit อื่นๆ
st.set_page_config(
    page_title="CAD File Uploader Example",
    page_icon="🚀",  # ใช้ Unicode แทน :rocket:
    layout="wide"
)

st.markdown("<h1 style='text-align:center;'>CAD File Uploader Examplepage</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a file", type=["json"])
if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
    # แสดงข้อมูลของไฟล์ที่อัปโหลด