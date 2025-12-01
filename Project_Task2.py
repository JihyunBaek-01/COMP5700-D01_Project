import pandas as pd

#Path for the all_repository table in the AIDev dataset on HuggingFace
ALL_REPO_PATH = "hf://datasets/hao-li/AIDev/all_repository.parquet"

#Output CSV filename
OUTPUT_CSV = "Project_Task2.csv"

def main():
    #Define Columns
    needed_columns = ["id", "language", "stars", "url"]

    print(f"[Task2] Loading 'all_repository' table from HuggingFace")
    
    #Question to AI: Is there a way to effectively load a large dataset?
    #AI suggestion: Load only necessary columns to optimize memory usage.
    try:
        df = pd.read_parquet(ALL_REPO_PATH, columns=needed_columns)
    except Exception as e:
        print(f"[Error] {e}")
        return

    #Rename Columns
    print("[Task2] Renaming columns")
    task2_df = df.rename(
        columns={
            "id": "REPOID",
            "language": "LANG",
            "stars": "STARS",
            "url": "REPOURL"
        }
    )

    #Save to CSV
    print(f"[Task2] Saving to '{OUTPUT_CSV}'")
    task2_df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8')
    
    print(f"Task 2 Completed. Rows: {len(task2_df)}")

if __name__ == "__main__":
    main()