import os
import json
import streamlit as st
from src.parser import extract_text_from_pdf
from src.requirement_extractor import extract_requirements
from src.testcase_generator import generate_test_cases   # 👈 NEW

UPLOAD_FOLDER = "data/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("outputs", exist_ok=True)

st.set_page_config(page_title="Autopilot QA", layout="centered")
st.title("🤖 Autopilot QA - From SRS → Test Cases")

uploaded_files = st.file_uploader(
    "Upload one or more PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    all_requirements = []

    for uploaded_file in uploaded_files:
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        srs_text = extract_text_from_pdf(file_path)
        with st.spinner(f"Extracting requirements from {uploaded_file.name}..."):
            requirements = extract_requirements(srs_text)

        all_requirements.append({uploaded_file.name: requirements})

    requirements_path = "outputs/requirements.json"
    with open(requirements_path, "w", encoding="utf-8") as f:
        json.dump(all_requirements, f, indent=2, ensure_ascii=False)

    st.subheader("📌 Extracted Requirements")
    st.json(all_requirements)

    if st.button("🚀 Generate Test Cases"):
        with st.spinner("Generating test cases..."):
            test_cases = generate_test_cases(requirements_path)

        st.subheader("🧪 Generated Test Cases")
        st.json(test_cases)

        st.download_button(
            label="⬇️ Download Test Cases JSON",
            data=json.dumps(test_cases, indent=2, ensure_ascii=False),
            file_name="testcases.json",
            mime="application/json"
        )
