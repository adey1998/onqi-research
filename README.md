# Onqi Research

This repository contains research prototypes and experiments for building AI-powered clinical decision support tools for healthcare.  
Each publication is organized into its own folder under `publications/`.


**Publication 1: Closing the Lung Cancer Screening Gap in FQHCs**  
- Synthetic dataset generation  
- NLP extraction for smoking history  
- Eligibility rules engine (USPSTF)  
- Evaluation (precision, recall, F1)  
- Results (tables, charts, workflow diagram)


## Upcoming Publications

1. NLP for Clinical Note Triage in Resource-Limited Clinics  
2. Referral Automation Workflows in Value-Based Care  
3. Policy Perspectives on Screening Gaps  
4. Lightweight Modular Architecture for Clinical Decision Support


## 🛠️ Setup

```bash
git clone https://github.com/arvildey/onqi-research.git
cd onqi-research
pip install -r requirements.txt
```

### Run Paper 1 MVP
```bash
# 1. Generate synthetic dataset
python publications/lung_cancer_fqhc/scripts generate_dataset.py
```


