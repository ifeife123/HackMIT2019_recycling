'''
main executable
'''

from image_detection import webcam, image_processing
import time
from recycling_status.determinator import check_list

while True:
    wb = webcam.WebCam()
    labels = []
    objects = []
    for filename in wb.imageFileQueue:
        labels.extend(image_processing.get_labels(filename))
    wb.clear_queue()
    igen_recycle = check_list(labels)
    print(labels)
    print(igen_recycle)
    '''
    Send the label values somewhere to be processed
    and get a string in return: ("recycle", "compostable", or "trash")
    and display the results in a window
    '''
    if igen_recycle == "recycle":
        wb.display_result("result_img/recycle.png")
    elif igen_recycle == "not_recycle":
        wb.display_result("result_img/no_recycle.png")
    elif igen_recycle == "dont_know":
        new_label = wb.display_result("result_img/unknown.png")

    time.sleep(1)
    wb.start_recording()
