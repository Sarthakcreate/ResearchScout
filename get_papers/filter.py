# get_papers/filter.py

from typing import List
from .types import Paper
from .fetch import fetch_pubmed_ids, fetch_paper_details

def get_filtered_papers(query: str, debug: bool = False) -> List[Paper]:
    pmids = fetch_pubmed_ids(query)
    results = []
    for pmid in pmids:
        try:
            paper = fetch_paper_details(pmid)
            if paper.non_academic_authors:
                if debug:
                    print(f"[DEBUG] Selected: {paper.title}")
                results.append(paper)
        except Exception as e:
            if debug:
                print(f"[ERROR] Failed to fetch {pmid}: {e}")
    return results
