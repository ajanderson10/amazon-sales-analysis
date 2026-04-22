import pandas as pd

df = pd.read_csv("amazon_fashion_cleaned.csv")

# Overall stats
print("=== Overall Price Statistics ===")
print(df[["actual_price", "discount_price", "discount_pct"]].describe().round(2))

# Top 10 most discounted products
print("\n=== Top 10 Most Discounted Products ===")
top_discount = df.sort_values("discount_pct", ascending=False).head(10)
print(top_discount[["name", "actual_price", "discount_price", "discount_pct"]])

# Top 10 highest rated products (min 100 ratings)
print("\n=== Top 10 Highest Rated Products ===")
top_rated = df[df["no_of_ratings"] >= 100].sort_values(
    "ratings", ascending=False).head(10)
print(top_rated[["name", "ratings", "no_of_ratings", "actual_price"]])

# Price buckets - how many products fall in each range
print("\n=== Products by Price Range ===")
bins = [0, 500, 1000, 2500, 5000, 99999]
labels = ["Under ₹500", "₹500-1000", "₹1000-2500", "₹2500-5000", "Over ₹5000"]
df["price_range"] = pd.cut(df["actual_price"], bins=bins, labels=labels)
print(df["price_range"].value_counts().sort_index())

# Most reviewed products
print("\n=== Top 10 Most Reviewed Products ===")
most_reviewed = df.sort_values("no_of_ratings", ascending=False).head(10)
print(most_reviewed[["name", "no_of_ratings", "ratings", "actual_price"]])
