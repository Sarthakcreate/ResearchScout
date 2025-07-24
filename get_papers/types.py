from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Author:
    name: str
    affiliation: Optional[str]

@dataclass
class Paper:
    pubmed_id: str
    title: str
    publication_date: str
    authors: List[Author]
    non_academic_authors: List[Author]
    company_affiliations: List[str]
    corresponding_email: Optional[str]
