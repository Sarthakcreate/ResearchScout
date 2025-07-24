import requests
from typing import List
from .types import Author, Paper

API_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
EMAIL = "xyz@gmail.com"
API_KEY = "your_api_key"

def fetch_pubmed_ids(query: str, max_results: int = 20) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results,
        "api_key": API_KEY,
        "email": EMAIL
    }
    url = f"{API_BASE}/esearch.fcgi"
    res = requests.get(url, params=params)
    res.raise_for_status()
    return res.json().get("esearchresult", {}).get("idlist", [])

def fetch_paper_details(pmid: str) -> Paper:
    params = {
        "db": "pubmed",
        "id": pmid,
        "retmode": "xml",
        "api_key": API_KEY,
        "email": EMAIL
    }
    url = f"{API_BASE}/efetch.fcgi"
    res = requests.get(url, params=params)
    res.raise_for_status()
    
    from xml.etree import ElementTree as ET
    root = ET.fromstring(res.content)
    article = root.find(".//PubmedArticle")
    title = article.findtext(".//ArticleTitle", default="No Title")
    pub_date = article.findtext(".//PubDate/Year", default="Unknown")

    authors = []
    for elem in article.findall(".//Author"):
        name = f"{elem.findtext('ForeName', '')} {elem.findtext('LastName', '')}".strip()
        affil = elem.findtext("AffiliationInfo/Affiliation")
        authors.append(Author(name=name, affiliation=affil))

    # Simple non-academic heuristic
    non_academic = [a for a in authors if a.affiliation and not any(word in a.affiliation.lower() for word in ["university", "institute", "college", "school", "hospital"])]

    # Company names (basic heuristic)
    company_affils = list({a.affiliation for a in non_academic if a.affiliation})

    # Extract email
    import re
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", " ".join([a.affiliation or "" for a in authors]))
    email = emails[0] if emails else None

    return Paper(
        pubmed_id=pmid,
        title=title,
        publication_date=pub_date,
        authors=authors,
        non_academic_authors=non_academic,
        company_affiliations=company_affils,
        corresponding_email=email
    )
