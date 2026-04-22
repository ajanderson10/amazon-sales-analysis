import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("DB_PASSWORD")

df = pd.read_csv("amazon_fashion_cleaned.csv")
df = df.drop(columns=["price_range"], errors="ignore")

engine = create_engine(
    f"mysql+mysqlconnector://root:{password}@localhost/amazon_db")

df.to_sql("products", con=engine, if_exists="replace", index=False)

print("Data loaded successfully!")
print(f"{len(df)} rows inserted into amazon_db.products")
