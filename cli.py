# cli.py (at root level)

import typer
import pandas as pd
from typing import Optional
from get_papers.filter import get_filtered_papers

app = typer.Typer(help="Fetch PubMed papers with pharma/biotech authors.")

@app.command()
def run(
    query: str = typer.Argument(..., help="Search query for PubMed"),
    file: Optional[str] = typer.Option(None, "--file", "-f", help="CSV output filename"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode")
):
    papers = get_filtered_papers(query, debug=debug)

    rows = []
    for p in papers:
        rows.append({
            "PubmedID": p.pubmed_id,
            "Title": p.title,
            "Publication Date": p.publication_date,
            "Non-academic Author(s)": "; ".join(a.name for a in p.non_academic_authors),
            "Company Affiliation(s)": "; ".join(p.company_affiliations),
            "Corresponding Author Email": p.corresponding_email or ""
        })

    df = pd.DataFrame(rows)
    if file:
        df.to_csv(file, index=False)
        typer.echo(f"Saved {len(papers)} results to {file}")
    else:
        typer.echo(df)

def main():
    app()

import sys
print("[DEBUG] sys.path =", sys.path)