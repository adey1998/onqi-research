import pandas as pd
import os
import json

ELIGIBILITY_DATA_PATH = "publications/lung_cancer_fqhc/data/processed/eligibility_flags.csv"
OUTPUT_DIR = "publications/lung_cancer_fqhc/data/processed"

# Converts numpy values to native types so JSON can read them
def to_native(obj):
    """Recursively convert numpy types to native Python types for JSON serialization."""
    if isinstance(obj, dict):
        return {k: to_native(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [to_native(v) for v in obj]
    elif hasattr(obj, "item"):  # numpy types
        return obj.item()
    return obj

def save_summary_stats():
    print("Loading eligibility data...")
    df = pd.read_csv(ELIGIBILITY_DATA_PATH)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Eligibility Summary
    total_patients = len(df)
    eligible_count = df["eligible"].sum()
    ineligible_count = total_patients - eligible_count
    eligible_percent = round((eligible_count / total_patients) * 100, 1)
    ineligible_percent = round((ineligible_count / total_patients) * 100, 1)

    # Pack-Years Summary
    pack_years_stats = df["pack_years"].describe().to_dict()

    # Quit-Years Summary (Former Smokers)
    quit_years_stats = (
        df[df["smoking_status"] == "former smoker"]["quit_years"]
        .dropna()
        .describe()
        .to_dict()
    )

    # Age Summary
    age_stats = df["age"].describe().to_dict()

    # Missed High-Risk Smokers (Gap)
    missed_high_risk = df[(df["eligible"] == False) & (df["pack_years"] >= 20)]
    missed_high_risk_percent = round((len(missed_high_risk) / total_patients) * 100, 1)

    # Top 3 comorbidities (for Table 1)
    top_comorbidities = (
        df["comorbidities"]
        .dropna()
        .str.split(",")
        .explode()
        .str.strip()
        .value_counts()
        .head(3)
    )
    comorbidities_summary_str = ", ".join([
        f"{cond} ({round((count / len(df)) * 100, 1)}%)"
        for cond, count in top_comorbidities.items()
    ])

    # -----------------------------------------------
    # Now we start generating the CSV & JSON files

    # Top Ineligibility Reasons
    top_ineligibility_reasons = (
        df[df["eligible"] == False]["eligibility_reason"]
        .value_counts()
        .reset_index()
    )
    top_ineligibility_reasons.columns = ["reason", "count"]
     # Save Top Ineligibility Reasons (CSV)
    top_ineligibility_reasons.to_csv(os.path.join(OUTPUT_DIR, "top_ineligibility_reasons.csv"), index=False)


    # Demographics Table (Table 1)
    demographics = pd.DataFrame({
        "Metric": [
            "Total Patients",
            "Eligible Patients (%)",
            "Ineligible Patients (%)",
            "Missed High-Risk Smokers (%)",
            "Age (Mean ± SD)",
            "Pack-Years (Mean ± SD)",
            "Quit-Years (Mean ± SD)",
            "Top Comorbidities"
        ],
        "Value": [
            total_patients,
            f"{eligible_count} ({eligible_percent}%)",
            f"{ineligible_count} ({ineligible_percent}%)",
            f"{missed_high_risk_percent}%",
            f"{round(age_stats['mean'], 1)} ± {round(age_stats['std'], 1)}",
            f"{round(pack_years_stats['mean'], 1)} ± {round(pack_years_stats['std'], 1)}",
            f"{round(quit_years_stats['mean'], 1)} ± {round(quit_years_stats['std'], 1) if 'std' in quit_years_stats else 'N/A'}",
            comorbidities_summary_str
        ]
    })
    # Save Table 1 (CSV)
    demographics.to_csv(os.path.join(OUTPUT_DIR, "table_1_demographics.csv"), index=False)

    # Summary Stats
    summary = {
        "total_patients": total_patients,
        "eligible": {"count": eligible_count, "percent": eligible_percent},
        "ineligible": {"count": ineligible_count, "percent": ineligible_percent},
        "missed_high_risk": {"count": len(missed_high_risk), "percent": missed_high_risk_percent},
        "pack_years": pack_years_stats,
        "quit_years": quit_years_stats
    }
    # Convert all numpy values to native types
    summary = to_native(summary)
    # Save Summary Stats (JSON)
    with open(os.path.join(OUTPUT_DIR, "summary_stats.json"), "w") as f:
        json.dump(summary, f, indent=4)


    print("Summary statistics saved!")
    print(f" - {OUTPUT_DIR}/summary_stats.json")
    print(f" - {OUTPUT_DIR}/table_1_demographics.csv")
    print(f" - {OUTPUT_DIR}/top_ineligibility_reasons.csv")

if __name__ == "__main__":
    save_summary_stats()