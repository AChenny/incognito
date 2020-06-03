# External libraries
import json

# Internal libraries
import bucketHelper

# Constants
BUCKET_NAME = 'request-text-bucket'; # Change this to your bucket name
BUCKET_TEXT_FILE_NAME = 'text_data.txt' 

def lambda_handler(event, context):
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Successful request."
        }),       
    }