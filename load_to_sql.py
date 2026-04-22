import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("amazon_fashion_cleaned.csv")
df = df.drop(columns=["price_range"], errors="ignore")

# Connect to MySQL - update password to yours
engine = create_engine(
    "mysql+mysqlconnector://root:MatchaLover@localhost/amazon_db")

# Load into table
df.to_sql("products", con=engine, if_exists="replace", index=False)

print("Data loaded successfully!")
print(f"{len(df)} rows inserted into amazon_db.products")
