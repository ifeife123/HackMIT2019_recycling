'''
file to isolate image components and return one or more search terms
'''

import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.path.dirname(__file__),
                                                            "RECYCLE-228027d5d267.json")
# Instantiates a client
client = vision.ImageAnnotatorClient()


def get_labels(imgfile):
    # The name of the image file to annotate
    file_name = os.path.abspath(imgfile)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    all_labels = []
    for label in labels:
        all_labels.append(label.description)
    return all_labels


#print(get_labels('C:/Users/choco/Pictures/Camera Roll/bottle.jpg'))
