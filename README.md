# Onqi Research

This repository contains the research and technical builds powering Onqi's mission to close the cancer screening gap using AI-driven clinical decision support.


## Publications

| # | Title | Status | Description |
|---|-------|---------|-------------|
| 1 | [Closing the Lung Cancer Screening Gap in FQHCs](./publications/lung_cancer_fqhc/README.md) | In Progress | MVP for lung cancer screening eligibility detection (synthetic dataset, NLP pipeline, rules engine, evaluation). |
| 2 | Natural Language Processing for Clinical Note Triage | Planned | Lightweight NLP engine for extracting tobacco history from unstructured notes in resource-limited clinics. |
| 3 | Referral Automation Workflows in Value-Based Care | Planned | Automated LDCT referral generation with role-based routing and workflow integration. |
| 4 | Policy Perspective: Closing the Cancer Screening Gap | Planned | Policy and workflow-driven recommendations to address barriers in FQHCs and underserved populations. |
| 5 | Early Lessons from Building Onqi Screening | Planned | Technical architecture, design decisions, and scaling lessons from building Onqi Screening. |


## Tech Stack

- **Backend & APIs:** Python (FastAPI, Uvicorn, Pydantic)
- **Data & NLP:** Pandas, Scikit-learn, MedSpaCy, SciSpacy
- **Database:** PostgreSQL, SQLAlchemy (for future SaaS papers)
- **Cloud Infrastructure:** GCP (Cloud Run, Cloud SQL, Cloud Functions, Cloud Storage)
- **Visualization & Reporting:** Matplotlib, Jupyter Notebooks
- **Automation & CI/CD:** GitHub Actions, Cloud Build
- **Documentation:** Markdown, Diagrams (Figma, Draw.io)


## Setup

```bash
git clone https://github.com/arvildey/onqi-research.git
cd onqi-research
pip install -r requirements.txt
```
