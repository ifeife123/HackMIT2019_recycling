'''
main executable
'''

from image_detection import webcam, image_processing
import time

while True:
    wb = webcam.WebCam()
    labels = []
    for filename in wb.imageFileQueue:
        labels.extend(image_processing.get_labels(filename))
    wb.clear_queue()
    print(labels)
    '''
    Send the label values somewhere to be processed
    and get a string in return: ("recycle", "compostable", or "trash")
    and display the results in a window
    '''
    wb.display_result("result_img/recycle.png")
    time.sleep(1)
    wb.start_recording()
