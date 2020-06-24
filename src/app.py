# Debugger Initialization. These lines are needed to be able to debug an api locally on vscode
# import ptvsd
# ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
# ptvsd.wait_for_attach()
# MAKE SURE TO REMOVE/COMMENT THESE OUT WHEN DEPLOYING

# External libraries
import json
import base64
import os
from uuid import uuid4

# Internal libraries
import bucketHelper
import textProcessHelper
import imageHelper

# Constants
INPUT_BUCKET_NAME = os.environ['INPUT_FILE_BUCKET']
OUTPUT_BUCKET_NAME = os.environ['OUTPUT_FILE_BUCKET']

def text_process_handler(event, context):
    # Converts the base64 document to byte-like string
    pdfDocument = base64.b64decode(event['body'])

    # Convert the pdf to a png image
    image = imageHelper.convert_pdf_to_image(pdfDocument)

    # Generate a unique key using random numbers
    metadata = {
        'first_name': event['headers']['First-Name'],
        'last_name': event['headers']['Last-Name']
    }
    unique_id = str(uuid4())
    generated_document_key = metadata['first_name'] + metadata['last_name'] + '_' + unique_id + '.png'

    # Upload the image to s3 bucket
    bucketHelper.upload_file_to_bucket(OUTPUT_BUCKET_NAME, generated_document_key, image)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Successful request."
        }),       
    }
