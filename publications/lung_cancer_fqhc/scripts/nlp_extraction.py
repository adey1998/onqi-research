import pandas as pd
import re
import os
import medspacy

#Paths
RAW_DATA_PATH = "publications/lung_cancer_fqhc/data/raw/synthetic_patients.csv"
OUTPUT_PATH = "publications/lung_cancer_fqhc/data/processed/nlp_extracted.csv"

def derive_status(pack_years, quit_years):
    """Derive smoking status from pack-years and quit-years."""
    if pack_years == 0:
        return "never smoker"
    if quit_years is None:
        return "current smoker"
    return "former smoker"

def extract_smoking_info(note):
    """Extract pack-years, quit-years, and smoking status from a clinical note."""
    pack_years = None
    quit_years = None
    
    if match := SMOKING_PATTERNS["pack_years"].search(note):
        pack_years = int(match.group(1))
    if match := SMOKING_PATTERNS["quit_years"].search(note):
        quit_years = int(match.group(1))
    return pack_years, quit_years

# 1. Load dataset
print("Loading dataset...")
df = pd.read_csv(RAW_DATA_PATH)

# 2. Initialize MedSpaCy pipeline
print("Initializing MedSpaCy pipeline...")
nlp = medspacy.load() # for basic clinical text processing

# 3. Regex patterns for smoking extraction
SMOKING_PATTERNS = {
    "pack_years": re.compile(r"(\d+)\s*pack[- ]?years?", re.IGNORECASE),
    "quit_years": re.compile(r"quit\s*(\d+)\s*years?", re.IGNORECASE),
}

# 4. Process each note with MedSpaCy + regex
print("Extracting NLP features...")
extracted_data = []

for _, row in df.iterrows():
    doc = nlp(row["note"]) # Process note with MedSpaCy (for future)
    pack_years, quit_years = extract_smoking_info(row["note"])
    status = derive_status(pack_years if pack_years is not None else row["pack_years"], quit_years)
    
    extracted_data.append({
        "name": row["name"],
        "age": row["age"],
        "pack_years": pack_years if pack_years is not None else row.get("pack_years", None),
        "quit_years": quit_years if quit_years is not None else row.get("quit_years", None),
        "smoking_status": status,
        "comorbidities": row["comorbidities"],
        "note": row["note"]
    })
    
# 5. Save output
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
pd.DataFrame(extracted_data).to_csv(OUTPUT_PATH, index=False)

print(f"NLP extraction complete! Results saved to {OUTPUT_PATH}")