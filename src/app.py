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
    metadata = {
        'first_name': event['headers']['First-Name'],
        'last_name': event['headers']['Last-Name']
    }

    # Converts the base64 document to byte-like string
    pdfDocument = base64.b64decode(event['body'])

    # Convert the pdf to a png image object
    imageObject = imageHelper.get_image_object_from_pdf(pdfDocument)

    imageString = imageHelper.convert_object_to_image_string(imageObject)

    imageWidth, imageHeight = imageObject.size

    # Use textract to parse document
    imageBlocks = textProcessHelper.get_document_text(imageString)

    # Build filters and get the bounding boxes 
    filters = [metadata['first_name'], metadata['last_name']]
    boundingBoxes = textProcessHelper.get_bounding_box_locations(imageBlocks, filters, imageWidth, imageHeight)

    # Black out the bouding box coordinates
    processedImageObject = imageHelper.black_out_coordinates_on_image(imageObject, boundingBoxes)
    processedImageString = imageHelper.convert_object_to_image_string(processedImageObject)
    
    # Generate a unique key using random numbers
    unique_id = str(uuid4())
    generated_document_key = metadata['first_name'] + metadata['last_name'] + '_' + unique_id + '.png'

    # Upload the image to s3 bucket
    bucketHelper.upload_file_to_bucket(OUTPUT_BUCKET_NAME, generated_document_key, processedImageString)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Successful request."
        }),       
    }
