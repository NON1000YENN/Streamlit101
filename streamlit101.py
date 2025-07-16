import streamlit as st

# ตั้งค่าเพจ (ต้องอยู่บรรทัดแรกสุด)
st.set_page_config(
    page_title="CAD File Uploader Example",
    page_icon=":rocket:",
    layout="wide"
)

# ใช้ HTML ทำให้ Title อยู่กลาง
st.markdown(
    """
    <h1 style='text-align: center;'>
        CAD File Uploader Examplepage
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("Import file uploader")

# อัปโหลดไฟล์ json
uploaded_file = st.file_uploader("Upload a file", type=["json"])

if uploaded_file:
    st.success(f"คุณอัปโหลดไฟล์: {uploaded_file.name}")
