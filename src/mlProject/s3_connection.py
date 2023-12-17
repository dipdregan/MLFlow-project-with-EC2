import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def create_s3_client():
    try:
        # Create an S3 client
        s3 = boto3.client(
            's3',
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION")
        )
        return s3
    except Exception as e:
        print(f"Error creating S3 client: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    s3_client = create_s3_client()

    if s3_client:
        print("S3 client created successfully.")
        # Perform S3 operations using s3_client
    else:
        print("Failed to create S3 client.")
