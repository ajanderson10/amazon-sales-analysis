# Amazon Fashion Sales Analysis

A data analysis pipeline built to explore pricing, discounts, and customer ratings 
from Amazon's fashion marketplace using Python, MySQL, and AWS S3.

## Project Overview
This project demonstrates an end-to-end data pipeline:
- Raw data ingestion and cleaning with Python and Pandas
- Relational database storage and querying with MySQL
- Cloud storage integration with AWS S3
- Version control and documentation with Git and GitHub

## Tools & Technologies
- **Python** — data cleaning and analysis (Pandas, SQLAlchemy, Boto3)
- **MySQL** — relational database storage and SQL querying
- **AWS S3** — cloud storage for raw and cleaned datasets
- **VS Code** — development environment
- **Git/GitHub** — version control

## Dataset
Amazon Products Sales Dataset 2023 sourced from Kaggle.
2,341 products across fashion and lifestyle categories with pricing, 
discount, and rating data.

## Key Findings
- Average discount across all products is **45.5%**
- Products in the ₹2,500–5,000 range receive the highest average discounts at **58%**
- Budget products under ₹500 receive the lowest discounts at **27%**
- The ₹1,000–2,500 range is the most competitive with **728 products**
- Jewelry dominates the most discounted products, with discounts up to **98%**
  
## Project Structure

    amazon-sales-analysis/
    ├── explore.py            # Initial data exploration
    ├── analyze.py            # Pandas analysis and insights
    ├── load_to_sql.py        # MySQL database loader
    ├── upload_to_s3.py       # AWS S3 upload script
    ├── queries.sql           # SQL analysis queries
    ├── .env                  # Local credentials (not tracked)
    └── .gitignore            # Excludes sensitive files and raw data
