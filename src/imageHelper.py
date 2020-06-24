# Description: This library consists of functions for all image file processing functions
import pdf2image
from PIL import Image
import io
import base64

# TODO: Update this to handle more than 1 image
# Description: Converts a pdf to image byte string
# Input: PDF byte string
# Output: Image byte string
def convert_pdf_to_image(pdfDocument):
    images = pdf2image.convert_from_bytes(pdfDocument, dpi=200, fmt='png')
    
    return_dict = {'images': []}
    for img in images:
        imgArr = io.BytesIO()
        img.save(imgArr, format='png')

        return_dict['images'].append(
            imgArr.getvalue()
        )
    
    return return_dict['images'][0]