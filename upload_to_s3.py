import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Connect to S3
s3 = boto3.client("s3")

# Your bucket name - must be globally unique
BUCKET_NAME = "amazon-fashion-analysis-ayyanah"

# Create bucket
try:
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={"LocationConstraint": "us-east-2"}
    )
    print(f"Bucket '{BUCKET_NAME}' created successfully!")
except ClientError as e:
    print(f"Bucket note: {e.response['Error']['Message']}")

# Upload both files
files = ["Amazon Fashion.csv", "amazon_fashion_cleaned.csv"]

for file in files:
    try:
        s3.upload_file(file, BUCKET_NAME, file)
        print(f"Uploaded: {file}")
    except FileNotFoundError:
        print(f"File not found: {file}")
    except NoCredentialsError:
        print("AWS credentials not found")

print("\nAll done!")

