from collections import Counter


def answer_question(question, text, findings, summary):
    question = question.lower()

    if "what sensitive data" in question or "sensitive data exists" in question:
        if not findings:
            return "No sensitive data was detected."

        types = sorted(set(item["type"] for item in findings))
        return "Sensitive data detected: " + ", ".join(types)

    elif "how many email" in question:
        count = sum(1 for item in findings if item["type"] == "Email Address")
        return f"There are {count} email address(es) in the document."

    elif "how many phone" in question:
        count = sum(1 for item in findings if item["type"] == "Phone Number")
        return f"There are {count} phone number(s) in the document."

    elif "summarize" in question:
        return summary

    elif "compliance risk" in question or "risks" in question:
        return summary

    elif "count" in question:
        counter = Counter(item["type"] for item in findings)
        if not counter:
            return "No sensitive data was found."

        return "\n".join([f"{k}: {v}" for k, v in counter.items()])

    else:
        return (
            "This MVP supports questions about sensitive data, counts, summary, "
            "and compliance risks. For advanced Q&A, this can be extended using RAG."
        )