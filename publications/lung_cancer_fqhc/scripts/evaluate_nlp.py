import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

def evaluate_nlp():
    """Evaluates NLP extraction accuracy by comparing nlp_extracted.csv with a manually labeled set.
    Metrics: Precision, Recall, F1-score for each target field."""
    
    # Load labeled data (ground truth)
    labeled_df = pd.read_csv("publications/lung_cancer_fqhc/data/labeled/labeled_notes.csv")
    
    # Load NLP predictions
    nlp_df = pd.read_csv("publications/lung_cancer_fqhc/data/processed/nlp_extracted.csv")
    
    merged_df = labeled_df.merge(nlp_df, on="name", suffixes=("_true", "_pred"))
    print(f"merged_df: {merged_df.columns.tolist()}")
    
    metrics = {}
    
    # Calculate metrics for each field
    for col in ["pack_years", "quit_years", "smoking_status"]:
        y_true = merged_df[f"{col}_true"]
        y_pred = merged_df[f"{col}_pred"]
        
        # For numeric fields (pack_years, quit_years), convert 
        if col in ["pack_years", "quit_years"]:
            y_true = y_true.astype(str)
            y_pred = y_pred.astype(str)
        
        metrics[col] = {
            "precision": precision_score(y_true, y_pred, average="micro"),
            "recall": recall_score(y_true, y_pred, average="micro"),
            "f1": f1_score(y_true, y_pred, average="micro")
        }
    
    # 3. Print results
    print("\n------- NLP Evaluation Metrics -------")
    for col, m in metrics.items():
        print(f"{col}: Precision={m['precision']:.2f}, Recall={m['recall']:.2f}, F1={m['f1']:.2f}")
        
if __name__ == "__main__":
    evaluate_nlp()