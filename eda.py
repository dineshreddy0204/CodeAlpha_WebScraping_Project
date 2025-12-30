import pandas as pd

# -------------------------------------------------
# STEP 1: Load Dataset
# -------------------------------------------------
df = pd.read_csv("data/books_large_data.csv")

print("===================================")
print("TASK 2: EXPLORATORY DATA ANALYSIS")
print("===================================")

# -------------------------------------------------
# STEP 2: Explore Dataset Structure
# -------------------------------------------------
print("\nDATASET STRUCTURE")
print(df.info())

# -------------------------------------------------
# STEP 3: Preview Data
# -------------------------------------------------
print("\nFIRST 5 RECORDS")
print(df.head())

print("\nLAST 5 RECORDS")
print(df.tail())

# -------------------------------------------------
# STEP 4: Data Quality Checks
# -------------------------------------------------
print("\nMISSING VALUES CHECK")
print(df.isnull().sum())

print("\nDUPLICATE RECORDS CHECK")
print(df.duplicated().sum())

# -------------------------------------------------
# STEP 5: Price Analysis (Statistics)
# -------------------------------------------------
print("\nPRICE STATISTICS")
print(df["Price (£)"].describe())

# -------------------------------------------------
# STEP 6: Rating Analysis
# -------------------------------------------------
print("\nRATING DISTRIBUTION")
print(df["Rating"].value_counts())

# -------------------------------------------------
# STEP 7: Identify Premium Products
# -------------------------------------------------
print("\nTOP 10 MOST EXPENSIVE BOOKS")
print(df.sort_values(by="Price (£)", ascending=False).head(10))

print("\nEDA COMPLETED SUCCESSFULLY")
with open("eda_report.txt", "w", encoding="utf-8") as f:
    f.write("EDA REPORT\n")
    f.write("="*50 + "\n")
    f.write(f"Total Records: {len(df)}\n")
    f.write(str(df.describe(include='all')))