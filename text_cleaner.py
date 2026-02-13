import re

def clean_text(text: str) -> str:
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove unwanted characters (optional)
    text = re.sub(r"[^a-zA-Z0-9.,;:()\- ]", "", text)

    return text.strip()
