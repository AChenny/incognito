# Description: This library consists of functions for all bucket interactions needed for the application
import boto3

# Description: Gets the metadata from an object in the bucket
# Input: Bucket name, key of the object
# Output: TODO: Metadata in json format(?)
def get_metadata(bucketName, key):
    client = boto3.client('s3')
    response = client.get_object(
    Bucket=bucketName,
    Key=key,
    )
    metadata = response['Metadata']
    return metadata

# Description: Uploads a file as an object to the bucket
# Input: Bucket name, key name, file content as bytes, (Optional): Dictionary for metadata
# Output: None
def upload_file_to_bucket(bucketName, key, content, metadata={}):
    s3 = boto3.client('s3')

    s3.put_object(
        Bucket = bucketName,
        Body = content,
        Key = key,
        Metadata = metadata
    )

# Description: Gets the binary data from an object in the bucket
# Input: Bucket name, key name
# Output: Bytes
def get_bucket_object(bucketName, objectKey):
    client = boto3.client('s3')
    response = client.get_object(
        Bucket=bucketName,
        Key=objectKey
    )
    return response['Body'].read()
