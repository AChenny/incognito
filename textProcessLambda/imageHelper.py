# Description: This library consists of functions for all image file processing functions
import pdf2image
from PIL import Image, ImageDraw
import io
import base64

# TODO: Update this to handle more than 1 image
# Description: Converts a pdf to image byte string
# Input: PIL Image Object
# Output: Image byte string
def convert_object_to_image_string(imageObject):
    imgStream = io.BytesIO()
    imageObject.save(imgStream, format='png')
    
    return imgStream.getvalue()

# TODO: Update this to handle more than 1 image
# Description: Convert a pdf image to PIL object
# Input: PDF byte string
# Output: PIL object
def get_image_object_from_pdf(pdfDocument):
    images = pdf2image.convert_from_bytes(pdfDocument, dpi=200, fmt='png')
    return images[0]

# Description: Blacks coordinates on a PIL object
# Input: PIL Image Object and coordinates
# Output: PIL Image Object (Blanked out)
def black_out_coordinates_on_image(imageObject, coordinates):
    drawObject = ImageDraw.Draw(imageObject)

    for coordinate in coordinates:
        drawObject.rectangle([coordinate['x1'], coordinate['y1'], coordinate['x2'], coordinate['y2']], fill='black')
    
    return imageObject