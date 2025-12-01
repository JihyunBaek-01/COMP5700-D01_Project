import pandas as pd

#Path for the all_pull_request table in the AIDev dataset on HuggingFace
ALL_PR_PATH = "hf://datasets/hao-li/AIDev/all_pull_request.parquet"

#Output CSV filename
OUTPUT_CSV = "Project_Task1.csv"

def main():
    #Load only the columns required for the task
    needed_columns = [
        "id", 
        "title", 
        "agent", 
        "body", 
        "repo_id", 
        "repo_url"
    ]

    print(f"[Task1] Loading 'all_pull_request' table from HuggingFace")
    print(f"[Task1] Source: {ALL_PR_PATH}")
    
    #Read the parquet file
    try:
        #Question to AI: Is there a way to effectively load a large dataset?
        #AI suggestion: Load only necessary columns to optimize memory usage.
        all_pr_df = pd.read_parquet(ALL_PR_PATH, columns=needed_columns)
        print(f"[Task1] Data loaded successfully. Shape: {all_pr_df.shape}")
    except Exception as e:
        print(f"Failed to load data. Please check your internet connection or libraries.")
        print(f"Details: {e}")
        return

    #Map the original dataset column names to the required CSV headers
    print("[Task1] Renaming columns")
    task1_df = all_pr_df.rename(
        columns={
            "title": "TITLE",
            "id": "ID",
            "agent": "AGENTNAME",
            "body": "BODYSTRING",
            "repo_id": "REPOID",
            "repo_url": "REPOURL",
        }
    )

    #Save the result to CSV format without the pandas index
    print(f"[Task1] Saving to '{OUTPUT_CSV}'")
    task1_df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8')

    print(f"Task 1 Completed.")
    print("Preview of the first 5 rows:")
    print(task1_df.head(5))

if __name__ == "__main__":
    main()