from collections import Counter


def generate_summary(findings, risk_level):
    if not findings:
        return """
No sensitive data was detected in the uploaded document.

Compliance Observation:
The document appears to have low privacy risk.

Suggested Remediation:
No immediate action is required, but manual review is still recommended.
"""

    counter = Counter(item["type"] for item in findings)

    summary = f"Document Risk Level: {risk_level}\n\n"
    summary += "Detected Sensitive Data:\n"

    for data_type, count in counter.items():
        summary += f"- {data_type}: {count} occurrence(s)\n"

    summary += "\nCompliance Observations:\n"
    summary += "- The document contains personal or confidential information.\n"
    summary += "- Sharing this document publicly may create privacy or compliance risks.\n"

    summary += "\nSecurity Risks:\n"
    summary += "- Sensitive data may be exposed if the document is shared without masking.\n"
    summary += "- API keys, passwords, or financial data can lead to unauthorized access.\n"

    summary += "\nSuggested Remediation:\n"
    summary += "- Mask or redact sensitive values before sharing.\n"
    summary += "- Restrict access to authorized users only.\n"
    summary += "- Avoid storing plain-text credentials or financial identifiers.\n"
    summary += "- Maintain audit logs for document access.\n"

    return summary