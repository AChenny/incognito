# Description: This library consists of functions for all bucket interactions needed for the application
import boto3

# Description: Gets the metadata from an object in the bucket
# Input: Bucket name, key of the object
# Output: TODO: Metadata in json format(?)
def getMetadata(bucketName, key):
    client = boto3.client('s3')
    response = client.get_object(
    Bucket=bucketName,
    Key=key,
    )
    metadata = response['Metadata']
    return metadata