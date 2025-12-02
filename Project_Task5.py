'''
The author(s) would like to acknowledge the use of Gemini, a language model developed by Google, 
in the preparation of this assignment. The Gemini was used in the following way(s) in this assignment: 
to suggest logic for case-insensitive keyword searching, methods for merging dataframes with different column names, 
and techniques for handling missing values (NaN) when combining text columns.
'''

import pandas as pd
import os

#Configuration
INPUT_TASK1 = "Project_Task1.csv"
INPUT_TASK3 = "Project_Task3.csv"

OUTPUT_CSV = "Project_Task5.csv"

#Security Keywords provided in the assignment Reference
SECURITY_KEYWORDS = [
    "race", "racy", "buffer", "overflow", "stack", "integer", "signedness", 
    "underflow", "improper", "unauthenticated", "gain access", "permission", 
    "cross site", "css", "xss", "denial service", "dos", "crash", "deadlock", 
    "injection", "request forgery", "csrf", "xsrf", "forged", "security", 
    "vulnerability", "vulnerable", "exploit", "attack", "bypass", "backdoor", 
    "threat", "expose", "breach", "violate", "fatal", "blacklist", "overrun", 
    "insecure"
]

'''
Question to AI: How can I check if a text contains any keyword from a given list, 
while ignoring case sensitivity and handling missing values?

AI suggestion: Create a function that converts text to lowercase (.lower()) and 
iterates through the keyword list. Use .apply() to run this function on the dataframe column.
'''
def check_security_keywords(text):

    #Checks if any security keyword exists in the text
    #Returns 1 if found, 0 otherwise
    if pd.isna(text) or text == "":
        return 0
    
    #Convert text to lowercase for case-insensitive matching
    text_lower = str(text).lower()
    
    for keyword in SECURITY_KEYWORDS:
        if keyword in text_lower:
            return 1
    return 0

def main():
    print("Starting Task 5")

    #Load only necessary columns to optimize memory usage
    print(f"[Task5] Loading {INPUT_TASK1}")
    if not os.path.exists(INPUT_TASK1):
        print(f"{INPUT_TASK1} not found. Please run Task 1 first.")
        return
    
    df_task1 = pd.read_csv(INPUT_TASK1, usecols=["ID", "AGENTNAME", "TITLE", "BODYSTRING"])

    print(f"[Task5] Loading {INPUT_TASK3}")
    if not os.path.exists(INPUT_TASK3):
        print(f"{INPUT_TASK3} not found. Please run Task 3 first.")
        return

    df_task3 = pd.read_csv(INPUT_TASK3, usecols=["PRID", "PRTYPE", "CONFIDENCE"])

    '''
    Question to AI: I have two CSVs with different column names for the ID. 
    How can I merge them using Pandas?
    
    AI suggestion: Use pd.merge() with 'left_on' and 'right_on' parameters 
    to specify the key columns for each dataframe. 
    Use 'how="inner"' to keep only matching rows.
    '''
    #Join condition: Task 1 'ID' == Task 3 'PRID'
    #Inner Join ensures we only keep rows that exist in both datasets
    print("[Task5] Merging datasets")
    merged_df = pd.merge(
        df_task1, 
        df_task3, 
        left_on="ID", 
        right_on="PRID", 
        how="inner"
    )
    
    print(f"[Task5] Merged {len(merged_df)} rows.")

    #Analyze Security Keywords
    print("[Task5] Scanning for security keywords in TITLE and BODY")
    
    '''
    Question to AI: I need to scan both 'TITLE' and 'BODYSTRING' for keywords. How can I combine them safely?
    
    AI suggestion: Use .fillna("") to replace NaN values with an empty string before concatenation. 
    This ensures every row has a valid string object to search within.
    '''
    #Combine Title and Body strings for efficient searching (handling NaNs)
    combined_text = merged_df["TITLE"].fillna("") + " " + merged_df["BODYSTRING"].fillna("")
    
    #Apply the keyword check function to create the boolean flag
    merged_df["SECURITY"] = combined_text.apply(check_security_keywords)

    #Rename columns to match requirements
    final_df = merged_df.rename(columns={
        "AGENTNAME": "AGENT",
        "PRTYPE": "TYPE"
    })
    
    #Select only the required columns
    final_df = final_df[["ID", "AGENT", "TYPE", "CONFIDENCE", "SECURITY"]]

    #Save to CSV
    print(f"[Task5] Saving to '{OUTPUT_CSV}'")
    final_df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8')

    #Show Statistics
    security_count = final_df["SECURITY"].sum()
    print(f"\nTask 5 Completed.")
    print(f"Total Rows: {len(final_df)}")
    print(f"Security Related PRs found: {security_count}")
    print(f"File saved: {OUTPUT_CSV}")
    print("\nPreview: ")
    print(final_df.head())

if __name__ == "__main__":

    main()
