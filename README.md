# Onqi Research

This repository contains research prototypes and experiments for building AI-powered clinical decision support tools for lung cancer screening and beyond.  
Each publication is organized into its own folder under `publications/`.



## Publication 1: Closing the Lung Cancer Screening Gap in FQHCs

This MVP supports the first research paper:

1. **Synthetic Dataset Generation** – Create ~100–200 mock patient records (structured + unstructured).
2. **NLP Extraction Engine** – Extract smoking history and quit date from clinical notes.
3. **Eligibility Rules Engine** – Apply USPSTF lung cancer screening guidelines.
4. **Evaluation** – Measure NLP accuracy (precision, recall, F1).
5. **Results & Outputs** – Generate tables, charts, and workflow diagram for publication.

---

## 🛠️ Setup

```bash
git clone <repo-url>
cd onqi-research
pip install -r requirements.txt
```

### Running the Dataset Generator
```bash
python publications/lung_cancer_fqhc/scripts generate_dataset.py
```
### This will output:
```bash
publications/lung_cancer_fqhc/data/raw/synthetic_patients.csv
```


