def classify_document_risk(findings):
    if not findings:
        return "Low Risk"

    high_count = sum(1 for item in findings if item["risk"] == "High")
    medium_count = sum(1 for item in findings if item["risk"] == "Medium")

    if high_count >= 2:
        return "High Risk"
    elif high_count == 1 or medium_count >= 3:
        return "Medium Risk"
    else:
        return "Low Risk"