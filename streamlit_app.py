streamlit_app.py
import streamlit as st
import os

# 1. Setup Page Look
st.set_page_config(page_title="NEET Aspirant Hub", page_icon="🩺", layout="wide")

# 2. Header Title
st.title("🩺 NEET Ultimate Resource Hub")
st.markdown("*Your personal digital library for cracking NEET.*")

# 3. Sidebar Navigation Menu
st.sidebar.header("🎯 Navigation")
page = st.sidebar.radio("Go to:", ["Dashboard", "physics", "chemistry", "biology", "Daily Planner"])

# Cloud directory setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 4. Core Function to Fetch and Download PDFs from GitHub Folders
def load_subject_pdfs(subject_name):
    st.header(f"📚 {subject_name.capitalize()} Study Material")
    folder_path = os.path.join(BASE_DIR, subject_name)
    
    if not os.path.exists(folder_path):
        st.info(f"Create a folder named '{subject_name}' in GitHub and add your PDFs there!")
        return

    # Scan for PDF files
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    
    if not pdf_files:
        st.warning(f"No PDFs found inside the '{subject_name}' folder yet. Upload some files on GitHub!")
    else:
        for file in pdf_files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, "rb") as f:
                pdf_bytes = f.read()
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"📄 **{file}**")
            with col2:
                st.download_button(
                    label="📥 Download",
                    data=pdf_bytes,
                    file_name=file,
                    mime='application/pdf',
                    key=file
                )
            st.markdown("---")

# 5. Page Content Routing
if page == "Dashboard":
    st.subheader("📊 Performance Trackers")
    col1, col2 = st.columns(2)
    col1.metric(label="Target Exam", value="NEET")
    col2.metric(label="Daily Study Goal", value="10 Hours")
    st.info("💡 **Pro-Tip**: 90% of Biology questions come directly from NCERT lines. Revise them daily!")

elif page in ["physics", "chemistry", "biology"]:
    load_subject_pdfs(page)

elif page == "Daily Planner":
    st.header("⏳ Today's High-Yield Checklist")
    st.checkbox("Read 1 Biology Chapter (NCERT)")
    st.checkbox("Solve 45 Physics Numericals")
    st.checkbox("Solve 45 Chemistry MCQs")
    st.checkbox("Revise mistakes from the Error Log Book")
