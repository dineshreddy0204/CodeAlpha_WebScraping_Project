# TASK 3: DATA VISUALIZATION (FINAL FIX)
# CodeAlpha Internship Project

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------
# 1. Load dataset
# -----------------------------------
df = pd.read_csv("data/books_large_data.csv")

print("\nColumns found in CSV:")
print(df.columns)

# -----------------------------------
# 2. Detect PRICE column automatically
# -----------------------------------
price_col = None
for col in df.columns:
    if "price" in col.lower():
        price_col = col
        break

if price_col is None:
    raise ValueError("Price column not found in CSV")

print(f"\nUsing price column: {price_col}")

# -----------------------------------
# 3. Clean Price column (CRITICAL)
# -----------------------------------
df[price_col] = (
    df[price_col]
    .astype(str)
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .str.strip()
)

df[price_col] = pd.to_numeric(df[price_col], errors="coerce")

# -----------------------------------
# 4. Convert Rating to numeric
# -----------------------------------
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating_Num"] = df["Rating"].map(rating_map)

# -----------------------------------
# 5. Drop invalid rows
# -----------------------------------
df = df.dropna(subset=[price_col, "Rating_Num"])

print("\nSample cleaned data:")
print(df[[price_col, "Rating", "Rating_Num"]].head())

print(f"\nTotal valid records after cleaning: {len(df)}")

# -----------------------------------
# 6. Create visuals folder
# -----------------------------------
os.makedirs("visuals", exist_ok=True)
sns.set(style="whitegrid")

# -----------------------------------
# 7. Rating Distribution
# -----------------------------------
plt.figure(figsize=(8, 5))
sns.countplot(x="Rating", data=df, order=["One", "Two", "Three", "Four", "Five"])
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("visuals/rating_distribution.png")
plt.close()

# -----------------------------------
# 8. Price Distribution
# -----------------------------------
plt.figure(figsize=(8, 5))
plt.hist(df[price_col], bins=20, edgecolor="black")
plt.title("Price Distribution (£)")
plt.xlabel("Price (£)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("visuals/price_distribution.png")
plt.close()

# -----------------------------------
# 9. Price vs Rating (BOXPLOT – FIXED)
# -----------------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(x="Rating_Num", y=price_col, data=df)
plt.title("Price vs Rating")
plt.xlabel("Rating (1 = One, 5 = Five)")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.savefig("visuals/price_vs_rating.png")
plt.close()

# -----------------------------------
# 10. Top 10 Most Expensive Books
# -----------------------------------
top10 = df.sort_values(by=price_col, ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=price_col, y="Book Title", data=top10)
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.tight_layout()
plt.savefig("visuals/top_10_expensive_books.png")
plt.close()

# -----------------------------------
# 11. Done
# -----------------------------------
print("\nTASK 3 COMPLETED SUCCESSFULLY")
print("Charts saved in visuals/ folder")