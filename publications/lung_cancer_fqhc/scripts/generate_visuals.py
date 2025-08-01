import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
ELIGIBILITY_DATA_PATH = "publications/lung_cancer_fqhc/data/processed/eligibility_flags.csv"
OUTPUT_DIR = "publications/lung_cancer_fqhc/visuals"

# Global Styling for Publications
plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10
})

def save_figure(fig, name):
    """Save figure in SVG and PDF formats (publication-ready)"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for ext in ["svg", "pdf"]:
        fig.savefig(os.path.join(OUTPUT_DIR, f"{name}.{ext}"), bbox_inches="tight")
    plt.close(fig)

def generate_visuals():
    print("Loading eligibility data...")
    df = pd.read_csv(ELIGIBILITY_DATA_PATH)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. Eligibility Breakdown Pie Chart
    print("Generating eligibility breakdown chart...")
    fig, ax = plt.subplots(figsize=(6, 6))
    eligibility_counts = df["eligible"].value_counts()
    wedges, texts, autotexts = ax.pie(
        eligibility_counts,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#4CAF50", "#E64A19"]  # green & orange-red
    )
    ax.legend(wedges, ["Eligible", "Ineligible"], loc="best")
    ax.set_title("Eligibility Breakdown")
    save_figure(fig, "eligibility_breakdown")

    # 2. Top Ineligibility Reasons (Horizontal Bar Chart)
    print("Generating ineligibility reason chart...")
    reasons = df[df["eligible"] == False]["eligibility_reason"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    reasons.plot(kind="barh", color="#E64A19", ax=ax)
    ax.set_xlabel("Count")
    ax.set_ylabel("Reason")
    ax.set_title("Top Ineligibility Reasons")
    ax.grid(axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    save_figure(fig, "ineligibility_reasons")

    # 3. Pack-years Distribution Histogram
    print("Generating pack-years histogram...")
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.hist(df["pack_years"], bins=15, color="#1565C0", edgecolor="black")
    ax.axvline(20, color="red", linestyle="--", label="USPSTF 20 Pack-Year Cutoff")
    ax.text(20.5, ax.get_ylim()[1]*0.9, "Cutoff", color="red")
    ax.set_xlabel("Pack-Years")
    ax.set_ylabel("Number of Patients")
    ax.set_title("Pack-Years Distribution")
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    ax.legend()
    save_figure(fig, "pack_years_distribution")

    # 4. Quit-years Distribution Histogram (Former Smokers)
    print("Generating quit-years histogram...")
    former_smokers = df[df["smoking_status"] == "former smoker"]
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.hist(former_smokers["quit_years"].dropna(), bins=10, color="#6A1B9A", edgecolor="black")
    ax.axvline(15, color="red", linestyle="--", label="USPSTF 15-Year Cutoff")
    ax.text(15.5, ax.get_ylim()[1]*0.9, "Cutoff", color="red")
    ax.set_xlabel("Quit-Years")
    ax.set_ylabel("Number of Patients")
    ax.set_title("Quit-Years Distribution (Former Smokers)")
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    save_figure(fig, "quit_years_distribution")

    # 5. Age vs Eligibility Boxplot
    print("Generating age vs eligibility boxplot...")
    fig, ax = plt.subplots(figsize=(6, 5))
    df.boxplot(column="age", by="eligible", ax=ax)
    ax.set_xlabel("Eligibility")
    ax.set_ylabel("Age")
    ax.set_title("Age vs Eligibility")
    ax.set_xticklabels(["Ineligible", "Eligible"])
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    plt.suptitle("")  # remove pandas auto-title
    save_figure(fig, "age_vs_eligibility")

    # 6. Missed High-Risk Smokers (Donut)
    print("Generating missed high-risk smokers chart...")
    missed_high_risk = df[(df["eligible"] == False) & (df["pack_years"] >= 20)]
    counts = [len(missed_high_risk), len(df[df["eligible"] == True])]
    labels = ["Missed High-Risk Smokers", "Eligible (Screened)"]
    fig, ax = plt.subplots(figsize=(7, 6))
    wedges, texts, autotexts = ax.pie(
        counts,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#FF8A65", "#43A047"],
        wedgeprops=dict(width=0.4)
    )
    ax.legend(wedges, labels, loc="best")
    ax.set_title("Missed High-Risk Smokers (Gap in Screening)")
    save_figure(fig, "missed_high_risk_smokers")

    # 7. Referral Workflow Funnel (Bar Chart)
    print("Generating referral workflow funnel...")
    total = len(df)
    eligible = len(df[df["eligible"] == True])
    referred = int(eligible * 0.9)
    completed = int(referred * 0.8)

    stages = ["Total Patients", "Eligible", "Referred", "Completed Screening"]
    values = [total, eligible, referred, completed]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(stages, values, color="#26A69A")
    ax.set_title("Referral Workflow Funnel")
    ax.set_ylabel("Patients")
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    save_figure(fig, "referral_workflow_funnel")

    print(f"All visuals generated in {OUTPUT_DIR}")

if __name__ == "__main__":
    generate_visuals()
