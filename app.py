import streamlit as st
import pandas as pd

from src.document_loader import load_document
from src.detector import detect_sensitive_data, mask_sensitive_data
from src.risk_classifier import classify_document_risk
from src.summarizer import generate_summary
from src.qa_engine import answer_question

st.set_page_config(page_title="Sensitive Data Detection Assistant", layout="wide")

st.title("Sensitive Data Detection & Compliance Assistant")

st.write("Upload a PDF, TXT, or CSV file to detect sensitive data and compliance risks.")

uploaded_file = st.file_uploader("Upload Document", type=["pdf", "txt", "csv"])

if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)

    text = load_document(uploaded_file)

    if not text.strip():
        st.error("No readable text found in this file.")
        st.stop()

    findings = detect_sensitive_data(text)
    risk_level = classify_document_risk(findings)
    summary = generate_summary(findings, risk_level)
    masked_text = mask_sensitive_data(text, findings)

    st.success("Document processed successfully.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Findings", len(findings))
    col2.metric("Risk Level", risk_level)
    col3.metric("File Type", uploaded_file.name.split(".")[-1].upper())

    st.subheader("Detected Sensitive Data")

    if findings:
        st.dataframe(pd.DataFrame(findings), use_container_width=True)
    else:
        st.info("No sensitive data detected.")

    st.subheader("Compliance Summary")
    st.text_area("Summary", summary, height=220)

    st.subheader("Masked Document Preview")
    st.text_area("Masked Text", masked_text[:5000], height=250)

    st.subheader("Ask a Question")
    question = st.text_input("Example: How many email addresses are present?")

    if question:
        answer = answer_question(question, text, findings, summary)
        st.write(answer)