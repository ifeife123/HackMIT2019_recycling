'''
main executable
'''

from image_detection import webcam, image_processing

while True:
    wb = webcam.WebCam()
    labels = []
    for filename in wb.imageFileQueue:
        labels.extend(image_processing.get_labels(filename))
        # send it somewhere
        print(labels)
    # get a value ("recycle", "compostable", or "trash" in response)
    wb.display_result("result_img/recycle.png")
    wb.start_recording()
