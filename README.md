# Sensitive Data Detection & Compliance Assistant

## Overview
Sensitive Data Detection & Compliance Assistant is a document analysis application that identifies confidential or personally identifiable information (PII) from uploaded files and provides compliance-focused risk analysis.

The application supports document upload, sensitive data detection, risk classification, summary generation, masking, and document-based question answering.

---

## Features

### Document Upload
Supported formats:
- PDF
- TXT
- CSV

### Sensitive Data Detection
Detects:
- Aadhaar Numbers
- PAN Numbers
- Email Addresses
- Phone Numbers
- Credit Card Numbers
- Bank Details
- API Keys / Passwords
 - Employee IDs

### Risk Classification
Documents are classified into:
- Low Risk
- Medium Risk
- High Risk

Classification depends on:
- Type of sensitive data
- Frequency of occurrence
- Severity of exposure

### Summary Generation
Generates:
- Compliance observations
- Security risks
- Suggested remediation steps

### Question Answering
Supports queries such as:
- What sensitive data exists in the document?
- How many email addresses are present?
- Summarize this document
- What compliance risks are identified?

### Data Masking
Detected sensitive values are masked for safe preview.

---

# Tech Stack

- Python
- Streamlit
- Pandas
- PyPDF2
- Regex (`re`)

---
# Architecture Overview

```text
User Upload
   ↓
Document Loader (PDF / TXT / CSV)
   ↓
Text Extraction
   ↓
Sensitive Data Detection
   ↓
Risk Classification
   ↓
Summary Generator
   ↓
Question Answering
   ↓
User Interface
```

---

# Approach

## Sensitive Data Detection
Regex-based pattern matching is used to detect structured sensitive information such as:
- Aadhaar
- PAN
- Emails
- Phone numbers
- Credentials

This approach was chosen because it provides:
- Fast execution
- Explainable results
- Reliable pattern matching for structured data

## Risk Scoring
Risk level is assigned based on:
- Sensitivity of detected entities
- Number of occurrences
- Potential compliance impact

Examples:
- Aadhaar / PAN / Credentials → High Risk
- Emails / Phone Numbers → Medium Risk

---

# Project Structure

```bash
sensitive-data-compliance-assistant/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── document_loader.py
│   ├── detector.py
│   ├── risk_classifier.py
│   ├── summarizer.py
│   └── qa_engine.py
│
└── sample_docs/
```

---

# Setup Instructions

## Clone Repository

```bash
git clone <repository_url>
cd sensitive-data-compliance-assistant
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

---

# Workflow

1. Upload document  
2. Extract text  
3. Detect sensitive information  
4. Classify risk  
5. Generate summary  
6. Ask questions  
7. View masked output  

---

# Challenges Faced

### PDF Text Extraction
Some PDFs do not extract text cleanly using PyPDF2, which may affect detection accuracy.

### False Positives
Large numeric values may resemble account or card numbers, requiring stricter regex patterns.

### Unstructured Confidential Information
Structured data is easier to detect compared to business-sensitive contextual information.

---

# Limitations

Current limitations:
- No OCR support for scanned PDFs
- Limited contextual understanding of confidential business information
- Detection depends on text extraction quality

---

# Future Improvements

- OCR support
- Better false-positive filtering
- Multi-document analysis
- Audit logging
- Advanced redaction support
- Containerized deployment

---


# Deployment
`(https://d2pnpfrnntsw3txdya8fto.streamlit.app/)`

---

# Author
**Sumedha Singh**
