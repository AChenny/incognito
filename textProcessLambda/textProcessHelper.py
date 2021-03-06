# Description: This library consists of functions for all textract and text processing interactions
import boto3
import time

# Description: Starts the job of text detection on the document
# Input: S3 Bucket name, objectName (Key)
# Output: Job id
def startJob(s3BucketName, objectName):
    response = None
    client = boto3.client('textract')
    response = client.start_document_text_detection(
    DocumentLocation={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': objectName
        }
    })

    return response["JobId"]

# Description: Periodically checks if the text detection job is complete and prints status
# Input: Job id
# Output: String of the status (When it is finished)/ Expected 'SUCCEEDED' if successful
def isJobComplete(jobId):
    time.sleep(5)
    client = boto3.client('textract')
    response = client.get_document_text_detection(JobId=jobId)
    status = response["JobStatus"]
    print("Job status: {}".format(status))

    while(status == "IN_PROGRESS"):
        time.sleep(5)
        response = client.get_document_text_detection(JobId=jobId)
        status = response["JobStatus"]
        print("Job status: {}".format(status))

    return status

# Description: Gets the results from a text detection job
# Input: Job id
# Output: Block object with all the data in a mapping -> Refer to https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html
def getJobResults(jobId):

    pages = []

    time.sleep(5)

    client = boto3.client('textract')
    response = client.get_document_text_detection(JobId=jobId)
    
    pages.append(response)
    print("Resultset page recieved: {}".format(len(pages)))
    nextToken = None
    if('NextToken' in response):
        nextToken = response['NextToken']

    while(nextToken):
        time.sleep(5)

        response = client.get_document_text_detection(JobId=jobId, NextToken=nextToken)

        pages.append(response)
        print("Resultset page recieved: {}".format(len(pages)))
        nextToken = None
        if('NextToken' in response):
            nextToken = response['NextToken']

    return pages

# Description: Synchronous detection of document text
# Input: Bytes of the document (JPEG or PNG format)
# Output: Block object with all the data in a mapping -> refer to https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html
def get_document_text(imageBytes):
    client = boto3.client('textract')

    documentObject = {
        'Bytes': imageBytes
    }

    response = client.detect_document_text(Document=documentObject)

    return response

# Description: Get bounding box locations from string
# Input: Block object from textract response and filter list
# Output: Bounding box location as an array (x1, y1, x2, y2)
def get_bounding_box_locations(blockObject, filters, imageWidth, imageHeight):
    blocks = blockObject['Blocks']
    boundingBoxes = []

    # Loop through all filters to get bounding boxes for each one
    for filter in filters:
        for block in blocks:
            if 'Text' in block:
                if filter in block['Text']:
                    x1 = block['Geometry']['Polygon'][0]["X"] * imageWidth
                    y1 = block['Geometry']['Polygon'][0]["Y"] * imageHeight

                    x2 = block['Geometry']['Polygon'][2]["X"] * imageWidth
                    y2 = block['Geometry']['Polygon'][2]["Y"] * imageHeight

                    coordinates = {
                        'x1' : x1,
                        'y1' : y1,
                        'x2' : x2,
                        'y2' : y2,
                    }

                    boundingBoxes.append(coordinates)

    return boundingBoxes