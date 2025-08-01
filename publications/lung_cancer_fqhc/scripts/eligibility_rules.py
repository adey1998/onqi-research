import pandas as pd
import os

# Paths
NLP_DATA_PATH = "publications/lung_cancer_fqhc/data/processed/nlp_extracted.csv"
OUTPUT_PATH = "publications/lung_cancer_fqhc/data/processed/eligibility_flags.csv"

def is_eligible(age, pack_years, quit_years, smoking_status):
    """Return True if patient meets USPSTF screening criteria."""
    
    if age < 50:
        return False, "Ineligible: Age below 50"
    if age > 80:
        return False, "Ineligible: Age above 80"
    if pack_years < 20:
        return False, "Ineligible: <20 pack-years"
    if smoking_status == "current smoker":
        return True, "Eligible: Current smoker"
    if smoking_status == "former smoker":
        if quit_years is not None and quit_years < 15:
            return True, "Eligible: Quit within 15 years"
        else:
            return False, "Ineligible: Quit ≥ 15 years ago"
    return False, "Ineligible: Unknown status"

# ------ Tests ------
def test_eligibility_rules():
    assert is_eligible(55, 30, None, "current smoker")[0] is True       # Eligible
    assert is_eligible(45, 30, None, "current smoker")[0] is False      # Age < 50
    assert is_eligible(81, 30, None, "current smoker")[0] is False      # Age > 80
    assert is_eligible(65, 10, None, "current smoker")[0] is False      # < 20 pack-years
    assert is_eligible(65, 25, 20, "former smoker")[0] is False         # Quit > 15 yrs
    assert is_eligible(60, 25, 10, "former smoker")[0] is True          # Former smoker OK

def main():
    print("Loading NLP extracted data...")
    df = pd.read_csv(NLP_DATA_PATH)
    
    print("Applying eligibility rules...")
    results = df.apply(
        lambda row: is_eligible(
            row["age"],
            row["pack_years"],
            row["quit_years"],
            row["smoking_status"]
        ),
        axis=1
    )
    
    # Split tuple into 2 columns
    df["eligible"] = results.apply(lambda x: x[0])
    df["eligibility_reason"] = results.apply(lambda x: x[1])
    
    # Save flagged patients
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    
    # Generate summary metrics
    total_patients = len(df)
    eligible_count = df["eligible"].sum()
    eligible_percentage = (eligible_count / total_patients) * 100
    
    print(f"Eligibility flags saved to {OUTPUT_PATH}")
    print("\n Summary Metrics:")
    print(f" — Total patients: {total_patients}")
    print(f" — Eligible patients: {eligible_count} ({eligible_percentage:.1f}%)")
    print(f" — Ineligible patients: {total_patients - eligible_count}")
    
if __name__ == "__main__":
    test_eligibility_rules()
    main()