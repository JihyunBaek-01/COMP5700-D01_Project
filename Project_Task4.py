'''
The author(s) would like to acknowledge the use of Gemini, a language model developed by Google, 
in the preparation of this assignment. The Gemini was used in the following way(s) in this assignment: 
to suggest a method for removing special characters from text data to prevent encoding errors, and 
to suggest an efficient method for loading large datasets by selecting only necessary columns.
'''

import pandas as pd
import re

#Path for the pr_commit_details table in the AIDev dataset on HuggingFace
PR_COMMIT_PATH = "hf://datasets/hao-li/AIDev/pr_commit_details.parquet"

#Output CSV filename
OUTPUT_CSV = "Project_Task4.csv"

#Question to AI: How can I remove special characters from the 'patch' column to prevent string encoding errors?
#AI suggestion: Use .encode('ascii', 'ignore') to strip out non-ASCII characters.
def clean_text(text):
    #Removes non-ascii characters to avoid encoding errors as requested
    if text is None:
        return ""
    #Convert to string just in case
    text = str(text)
    #Remove non-ascii characters (keep standard text and code symbols)
    return text.encode('ascii', 'ignore').decode('ascii')

def main():
    #Define Columns
    needed_columns = [
        "pr_id", "sha", "message", "filename", 
        "status", "additions", "deletions", "changes", "patch"
    ]

    print(f"[Task4] Loading 'pr_commit_details' table")
    
    #Question to AI: Is there a way to effectively load a large dataset?
    #AI suggestion: Load only necessary columns to optimize memory usage.
    try:
        df = pd.read_parquet(PR_COMMIT_PATH, columns=needed_columns)
    except Exception as e:
        print(f"[Error] {e}")
        return

    #Clean Special Characters
    print("[Task4] Cleaning special characters in 'patch' column")
    #Apply the cleaning function (AI-suggested) to the 'patch' column
    df['patch'] = df['patch'].apply(clean_text)

    #Rename Columns
    print("[Task4] Renaming columns")
    task4_df = df.rename(
        columns={
            "pr_id": "PRID",
            "sha": "PRSHA",
            "message": "PRCOMMITMESSAGE",
            "filename": "PRFILE",
            "status": "PRSTATUS",
            "additions": "PRADDS",
            "deletions": "PRDELSS",
            "changes": "PRCHANGECOUNT",
            "patch": "PRDIFF"
        }
    )

    #Save to CSV
    print(f"[Task4] Saving to '{OUTPUT_CSV}'")
    task4_df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8')
    
    print(f"Task 4 Completed. Rows: {len(task4_df)}")

if __name__ == "__main__":

    main()
