import pandas as pd

def generate_mock_labels():
    """Generate a mock 'labeled_notes.csv' file for evaluating against the NLP pipeline."""
    
    # Load synthetic patients
    df = pd.read_csv("publications/lung_cancer_fqhc/data/raw/synthetic_patients.csv")
    
    # Create smoking_status column (derived automatically for now)
    df["smoking_status"] = df["quit_years"].apply(
        lambda x: "current smoker" if pd.isna(x) else "former smoker"
    )
    
    # Take a subset (first 50) for evaluation
    labeled_df = df[["name", "pack_years", "quit_years", "smoking_status"]].head(50)
    
    # Save labeled dataset
    labeled_df.to_csv("publications/lung_cancer_fqhc/data/labeled/labeled_notes.csv", index=False)
    print("Mock labeled dataset created -> ../data/labeled/labeled_notes.csv")
    print("Reminder: These auto-generated labels need to be replaced with human-reviewed ones for clinical evaluation.")
    
if __name__ == "__main__":
    generate_mock_labels()