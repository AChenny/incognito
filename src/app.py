import ptvsd

# Enable ptvsd on 0.0.0.0 address and on port 5890 that we'll connect later with our IDE
ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
ptvsd.wait_for_attach()

# External libraries
import json

# Internal libraries
import bucketHelper
import textProcessHelper

# Constants
BUCKET_NAME = 'incognito-file-storage-bucket' # Change this to your bucket name
TEST_RESUME_FILENAME = 'Resume.pdf'

def lambda_handler(event, context):
    # Extract text from pdf
    jobId = textProcessHelper.startJob(BUCKET_NAME, TEST_RESUME_FILENAME)
    print("Started job with id: {}".format(jobId))

    if (textProcessHelper.isJobComplete(jobId)):
        response = textProcessHelper.getJobResults(jobId)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Successful request."
        }),       
    }

def upload_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Successful request."
        }),       
    }
