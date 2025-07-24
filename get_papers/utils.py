# Utility functions: email extraction, keyword matching
import re

ACADEMIC_KEYWORDS = [
    "university", "institute", "college", "school", "department", "centre", "center", "research"
]
COMPANY_KEYWORDS = [
    "pharma", "biotech", "inc", "ltd", "gmbh", "corp", "pfizer", "novartis", "astrazeneca", "roche", "abbvie"
]

def extract_email(text: str) -> str:
    if not text:
        return ""
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group(0) if match else ""

def is_academic(affil: str) -> bool:
    return any(word.lower() in affil.lower() for word in ACADEMIC_KEYWORDS)

def is_company(affil: str) -> bool:
    return any(word.lower() in affil.lower() for word in COMPANY_KEYWORDS)
