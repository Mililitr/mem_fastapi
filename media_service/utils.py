import boto3
from botocore.exceptions import NoCredentialsError
import os

S3_BUCKET = os.getenv("S3_BUCKET")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_ENDPOINT = os.getenv("S3_ENDPOINT")

s3 = boto3.client('s3', endpoint_url=S3_ENDPOINT,
                  aws_access_key_id=S3_ACCESS_KEY,
                  aws_secret_access_key=S3_SECRET_KEY)

async def upload_file_to_s3(file):
    try:
        s3.upload_fileobj(file.file, S3_BUCKET, file.filename)
        file_url = f"{S3_ENDPOINT}/{S3_BUCKET}/{file.filename}"
        return file_url
    except NoCredentialsError:
        return None