# app.py
import streamlit as st
from get_papers.filter import get_filtered_papers
import pandas as pd

st.set_page_config(page_title="", layout="centered")

st.title("ResearchScout")
st.markdown("Your intelligent engine for the best research papers.")
st.markdown("Find the best and most relavant research papers according to your topic of interest.")

query = st.text_input("Enter your search query:", "")
debug = st.checkbox("Show debug logs")
submit = st.button("Fetch Papers")

if submit and query:
    with st.spinner("Fetching papers..."):
        papers = get_filtered_papers(query, debug=debug)

        if not papers:
            st.warning("No relevant papers found.")
        else:
            rows = [{
                "PubmedID": p.pubmed_id,
                "Title": p.title,
                "Publication Date": p.publication_date,
                "Non-academic Author(s)": "; ".join(a.name for a in p.non_academic_authors),
                "Company Affiliation(s)": "; ".join(p.company_affiliations),
                "Corresponding Author Email": p.corresponding_email or ""
            } for p in papers]

            df = pd.DataFrame(rows)
            st.success(f"Found {len(df)} relevant papers.")
            st.dataframe(df)

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name="results.csv",
                mime="text/csv"
            )
