# 🧪 ResearchScout

**ResearchScout** is a powerful yet lightweight tool that fetches recent research papers from PubMed based on any user query and highlights papers that have **industry** authors. It’s ideal for competitive intelligence, market research, and staying ahead in pharma R&D trends.

Built with **Python**, packaged via **Poetry**, and powered by **Streamlit** for a user-friendly interface.

---

## 🚀 Features

- 🔎 Search PubMed using any keyword or phrase  
- 🧠 Extract paper metadata and check for non-academic affiliations  
- 🧾 Export results as CSV  
- 🖥️ Intuitive web interface via Streamlit  
- 🧰 Modular, typed, and production-ready backend

---

## 🌐 Live Demo (coming soon)
> You can run the app locally using the instructions below. Deployment on Streamlit Cloud is also supported.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pharma-paper-scout.git
cd researchScout
````

### 2. Install Poetry

[Install Poetry](https://python-poetry.org/docs/#installation) if not already installed.

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 3. Set Up Environment

```bash
poetry install
```

### 4. Activate Virtual Environment

```bash
poetry shell
```

---

## 🧪 Usage (CLI)

```bash
poetry run get-papers-list "any-topic-you-want" --file results.csv --debug
```

* Replace `"any-topic-you-want"` with your desired PubMed search term.
* The `--file` option allows CSV export.
* `--debug` prints verbose logging with selected papers and errors.

---

## 🖥️ Usage (Streamlit Web App)

```bash
poetry run streamlit run app.py
```

* Enter your PubMed search term in the input field
* View results in a table
* Download as CSV with one click

---

## 📁 Project Structure

```
ResearchScout/
├── get_papers/
│   ├── __init__.py
│   ├── fetch.py
│   ├── filter.py
│   ├── types.py
├── app.py
├── cli.py
├── pyproject.toml
├── README.md
```

---

## 📌 Tech Stack

* Python 3.11
* Poetry (for dependency & packaging)
* Typer (CLI)
* Streamlit (UI)
* Requests (API interaction)
* 
---

## 📃 License

This project is licensed under the **MIT License**. Feel free to use, modify, and share.

---

## 🙋‍♂️ Author

**Sarthak Mangalmurti**
AI/ML Developer | Data Science Professional | ML Engineer
🔗 [LinkedIn](https://www.linkedin.com/in/sarthakmangalmurti) 
• 📬 Reach out for collaboration!

---

## ⭐ If You Like It

If you found this useful, don’t forget to **star ⭐ the repo** and share it with fellow AI/Pharma enthusiasts!

---
