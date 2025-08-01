import pandas as pd

# Paths
ELIGIBILITY_PATH = "publications/lung_cancer_fqhc/data/processed/eligibility_flags.csv"

def validate_data():
    print("Loading eligibility data...")
    df = pd.read_csv(ELIGIBILITY_PATH)

    # 1. Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # 2. Check outliers for pack_years and quit_years
    print("\nPack-years statistics:")
    print(df["pack_years"].describe())

    print("\nQuit-years statistics:")
    print(df["quit_years"].describe())

    # 3. Eligibility breakdown
    print("\nEligibility Breakdown:")
    print(df["eligible"].value_counts())

    print("\nTop reasons for inelgibility:")
    print(df[df["eligible"] == False]["eligibility_reason"].value_counts())

    # 4. Random sample for manual review
    print("\nRandom sample for review:")
    print(df.sample(5))

if __name__ == "__main__":
    validate_data()