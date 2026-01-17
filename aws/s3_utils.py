import boto3

BUCKET_NAME = "sales-call-madhavi"

s3_client = boto3.client("s3", region_name="us-east-1")

def upload_audio_to_s3(file_path, file_name):
    s3_client.upload_file(file_path, BUCKET_NAME, file_name)
    return f"s3://{BUCKET_NAME}/{file_name}"
