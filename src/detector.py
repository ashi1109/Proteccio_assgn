import re

PATTERNS = {
    "Aadhaar Number": r"(?<!\d)\d{4}\s?\d{4}\s?\d{4}(?!\d)",
    "PAN Number": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
    "Email Address": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "Phone Number": r"(?<!\d)(?:\+91[\s-]?)?[6-9]\d{9}(?!\d)",
    "Credit Card Number": r"(?<!\d)(?:\d[ -]*?){13,16}(?!\d)",
    "API Key / Password": r"\b(?:api[_-]?key|token|secret|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-@#$%^&*]{6,}",
    "Bank Account Number": r"\b(?:account|acc|bank)\s*(?:number|no)?\s*[:=-]?\s*\d{9,18}\b",
    "Employee ID": r"\b(?:EMP|EMPLOYEE)[-_]?\d{3,8}\b",
}


def detect_sensitive_data(text):
    findings = []

    for data_type, pattern in PATTERNS.items():
        matches = re.finditer(pattern, text, flags=re.IGNORECASE)

        for match in matches:
            value = match.group().strip()

            findings.append({
                "type": data_type,
                "value": value,
                "risk": get_item_risk(data_type)
            })

    return remove_duplicates(findings)


def get_item_risk(data_type):
    high_risk = {
        "Aadhaar Number",
        "PAN Number",
        "Credit Card Number",
        "API Key / Password",
        "Bank Account Number"
    }

    medium_risk = {
        "Email Address",
        "Phone Number",
        "Employee ID"
    }

    if data_type in high_risk:
        return "High"

    if data_type in medium_risk:
        return "Medium"

    return "Low"


def remove_duplicates(findings):
    seen = set()
    unique_findings = []

    for item in findings:
        key = (item["type"], item["value"])

        if key not in seen:
            seen.add(key)
            unique_findings.append(item)

    return unique_findings


def mask_sensitive_data(text, findings):
    masked_text = text

    for item in findings:
        value = item["value"]

        if len(value) <= 4:
            masked_value = "****"
        else:
            masked_value = "*" * (len(value) - 4) + value[-4:]

        masked_text = masked_text.replace(value, masked_value)

    return masked_text