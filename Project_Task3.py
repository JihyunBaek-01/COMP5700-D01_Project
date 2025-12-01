import pandas as pd

#Path for the pr_task_type table in the AIDev dataset on HuggingFace
PR_TASK_PATH = "hf://datasets/hao-li/AIDev/pr_task_type.parquet"

#Output CSV filename
OUTPUT_CSV = "Project_Task3.csv"

def main():
    #Define Columns
    needed_columns = ["id", "title", "reason", "type", "confidence"]

    print(f"[Task3] Loading 'pr_task_type' table from HuggingFace...")
    
    #Question to AI: Is there a way to effectively load a large dataset?
    #AI suggestion: Load only necessary columns to optimize memory usage.
    try:
        df = pd.read_parquet(PR_TASK_PATH, columns=needed_columns)
    except Exception as e:
        print(f"[Error] {e}")
        return

    #Rename Columns
    print("[Task3] Renaming columns")
    task3_df = df.rename(
        columns={
            "id": "PRID",
            "title": "PRTITLE",
            "reason": "PRREASON",
            "type": "PRTYPE",
            "confidence": "CONFIDENCE"
        }
    )

    #Save to CSV
    print(f"[Task3] Saving to '{OUTPUT_CSV}'")
    task3_df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8')
    
    print(f"Task 3 Completed. Rows: {len(task3_df)}")

if __name__ == "__main__":
    main()