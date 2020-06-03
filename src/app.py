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