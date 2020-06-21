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
from pdf2image import convert_from_bytes

# Internal libraries
import bucketHelper
import textProcessHelper

# Constants
INPUT_BUCKET_NAME = os.environ['INPUT_FILE_BUCKET']
OUTPUT_BUCKET_NAME = os.environ['OUTPUT_FILE_BUCKET']
INPUT_BUCKET_NAME = os.environ['INPUT_FILE_BUCKET']

def text_process_handler(event, context):
    # Test to check if poppler works, if this request passes, then poppler and pdf2image is working
    document = bucketHelper.get_bucket_object('incognito-input-files', 'Resume.pdf')
    images = convert_from_bytes(document,dpi=150)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Successful request."
        }),       
    }