# External libraries
import json
import base64

# Internal libraries

def upload_handler(event, context):
    # TODO: Spin up a website to host the image
    # TODO: Invoke text process lambda
    # TODO: Return the URL to the website with a key
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Successful request."
        }),       
    }
