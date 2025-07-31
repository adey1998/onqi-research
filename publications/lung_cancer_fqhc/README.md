# Closing the Lung Cancer Screening Gap in Federally Qualified Health Centers (FQHCs) Using AI-Powered Clinical Decision Support

This project is the MVP build for Publication 1 in the Onqi Research series.
It demonstrates how synthetic data, NLP, and rules-based eligibility logic can help identify patients who qualify for lung cancer screening in resource-limited clinics.

## Features
**Synthetic FQHC Dataset:** 100–200 mock patient records (structured data + unstructured clinical notes).

**NLP Extraction Engine:** Extracts smoking status, pack-years, and quit dates from free-text notes using MedSpaCy and regex.

**Eligibility Rules Engine:** Implements USPSTF guidelines (age 50–80, ≥20 pack-years, current smoker or quit < 15 years).

**Evaluation Pipeline:** Manual label set (50 notes) to measure NLP accuracy (precision, recall, F1).

**Results Generation:** Output eligibility tables and NLP performance metrics for publication.

**Workflow Diagram:** Visual representation of integration into an FQHC clinical workflow.

## Project Structure
```bash
publications/lung_cancer_fqhc/
│
├── data/
│   ├── synthetic/                # Generated synthetic datasets
│   └── labeled/                  # Manually labeled data for NLP evaluation
│
├── notebooks/                    # Jupyter notebooks for exploration and analysis
│
├── scripts/
│   ├── generate_dataset.py       # Create synthetic patient data
│   ├── nlp_extraction.py         # Extract smoking-related features from notes
│   ├── eligibility_rules.py      # Apply screening eligibility rules
│   ├── evaluate_nlp.py           # Compute NLP accuracy metrics
│   └── generate_results.py       # Generate tables & charts for paper
│
└── README.md                     # This file
```

## Setup
```bash
# Clone repository
git clone https://github.com/arvildey/onqi-research.git
cd onqi-research

# Install dependencies
pip install -r requirements.txt
```

## Running the MVP
**1. Generate Synthetic Dataset**
```bash
python publications/lung_cancer_fqhc/scripts/generate_dataset.py
```

**2. Run NLP Extraction**
```bash
python publications/lung_cancer_fqhc/scripts/nlp_extraction.py
```

**3. Apply Eligibility Rules**
```bash
python publications/lung_cancer_fqhc/scripts/eligibility_rules.py
```

**4. Evaluate NLP Accuracy**
```bash
python publications/lung_cancer_fqhc/scripts/evaluate_nlp.py
```

**5. Generate Results for Paper**
```bash
python publications/lung_cancer_fqhc/scripts/generate_results.py
```

## Expected Outputs
- **[NLP Accuracy Report](scripts/evaluate_nlp.py):** Precision, recall, and F1-score for smoking-related extraction.
- **[Eligibility Table](scripts/eligibility.py):** Flagged patients who meet USPSTF criteria.
- **[Workflow Diagram](docs/workflow_diagram.png):** Visual flow for FQHC integration.
- **[Figures & Tables](outputs/):** Ready for inclusion in MedRxiv paper.

## References
- [USPSTF Lung Cancer Screening Guidelines](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/lung-cancer-screening)
- [MedSpaCy Documentation](https://github.com/medspacy/medspacy)
- [SciSpacy Documentation](https://allenai.github.io/scispacy/)


## Next Steps
- Incorporate comorbidities (COPD, diabetes) into NLP-driven subgroup analysis.
- Deploy lightweight API for real-world testing in simulated environments.
- Expand NLP pipeline with de-identification and clinical concept mapping.
