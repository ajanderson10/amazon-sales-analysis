import pandas as pd

# Load the dataset
df = pd.read_csv("Amazon Fashion.csv")

# Drop columns we don't need
df = df.drop(columns=["image", "link"])

# Clean price columns - remove ₹ symbol and commas, convert to float
df["actual_price"] = df["actual_price"].str.replace(
    "₹", "").str.replace(",", "").str.strip().astype(float)
df["discount_price"] = df["discount_price"].str.replace(
    "₹", "").str.replace(",", "").str.strip().astype(float)

# Clean ratings columns - convert to numeric
df["ratings"] = pd.to_numeric(df["ratings"], errors="coerce")
df["no_of_ratings"] = pd.to_numeric(
    df["no_of_ratings"].str.replace(",", ""), errors="coerce")

# Drop rows where actual_price is missing
df = df.dropna(subset=["actual_price"])

# Fill missing ratings with 0
df["ratings"] = df["ratings"].fillna(0)
df["no_of_ratings"] = df["no_of_ratings"].fillna(0)
df["discount_price"] = df["discount_price"].fillna(df["actual_price"])

# Add a discount percentage column
df["discount_pct"] = (
    (df["actual_price"] - df["discount_price"]) / df["actual_price"] * 100).round(2)

# Save cleaned file
df.to_csv("amazon_fashion_cleaned.csv", index=False)

print("Cleaning complete!")
print("Shape:", df.shape)
print(df.head())
