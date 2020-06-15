# Debugger Initialization. These lines are needed to be able to debug an api locally on vscode
# import ptvsd
# ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
# ptvsd.wait_for_attach()

# External libraries
import json
import base64
import os
from uuid import uuid4

# Internal libraries
import bucketHelper
import textProcessHelper

# Constants
OUTPUT_BUCKET_NAME = os.environ['OUTPUT_FILE_BUCKET']

def text_process_handler(event, context):
    # # Extract text from pdf
    # jobId = textProcessHelper.startJob(BUCKET_NAME, TEST_RESUME_FILENAME)
    # print("Started job with id: {}".format(jobId))

    # if (textProcessHelper.isJobComplete(jobId)):
    #     response = textProcessHelper.getJobResults(jobId)
    bucketHelper.upload_file_to_bucket(OUTPUT_BUCKET_NAME, 'Success.txt', 'Success.')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Successful request."
        }),       
    }

def upload_handler(event, context):
    # If the body is empty, throw an error
    if event['body'] is None:
        return {
            "statusCode": 401,
            "body": json.dumps({
            "message": "Could not find file in event body."
            }),   
        }
    
    # Converts the base64 document to byte like string
    document = base64.b64decode(event['body'])
    
    metadata = {
        'first_name': event['headers']['First-Name'],
        'last_name': event['headers']['Last-Name']
    }

    # Generate a unique document key
    unique_id = str(uuid4())
    generated_document_key = metadata['first_name'] + metadata['last_name'] + '_' + unique_id + '.pdf'

    bucketHelper.upload_file_to_bucket(BUCKET_NAME, generated_document_key, document, metadata)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Successful Upload.",
            "s3-object-key": generated_document_key
        }),
    }
