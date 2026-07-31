import streamlit as st
import json
from parser import (
    extract_text,
    extract_email,
    extract_phone,
    extract_name,
    extract_skills
)

st.set_page_config(
    page_title="AI Resume Parser",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume Parser")
st.write("Upload a PDF resume to extract important information.")

uploaded_file = st.file_uploader(
    "Choose a Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)

    st.success("Resume Parsed Successfully!")

    st.subheader("Extracted Information")

    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")

    st.write("**Skills:**")
    if skills:
        for skill in skills:
            st.write(f"✅ {skill}")
    else:
        st.write("No skills found.")

    data = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Skills": skills
    }

    st.subheader("JSON Output")
    st.json(data)

    st.download_button(
        label="⬇ Download JSON",
        data=json.dumps(data, indent=4),
        file_name="resume_data.json",
        mime="application/json"
    )

st.markdown("---")
st.caption("Developed using Python, Streamlit and NLP")
