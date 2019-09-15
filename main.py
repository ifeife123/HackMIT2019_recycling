'''
main executable
'''

from image_detection import webcam, image_processing
import time
from recycling_status.determinator import check_list
import cv2
import csv

cap = cv2.VideoCapture(0)
imageIndex = 0
while True:
    imageIndex += 1
    success, frame = cap.read()
    cv2.imshow("viewfinder", frame)
    k = cv2.waitKey(10)

    if k == ord('q'):
        cv2.destroyAllWindows()
        break
    if k == ord('s'): #wait for start
        filename = "frames/frame%d.jpg" % imageIndex
        cv2.imwrite(filename, frame)
        labels = image_processing.get_labels(filename)
        igen_recycle = check_list(labels) #check based on labels if it is recyclable or not
        print(labels)
        print(igen_recycle)

        if igen_recycle == "recycle":
            cv2.imshow("out",cv2.imread("result_img/recycle.png"))
        elif igen_recycle == "not_recycle":
            cv2.imshow("out",cv2.imread("result_img/no_recycle.png"))
        elif igen_recycle == "dont_know":
            cv2.imshow("out",cv2.imread("result_img/unknown.png"))

            l = cv2.waitKey(0)
            is_recycled = 1 if l == ord('y') else 0
            rows = zip(labels, [is_recycled for i in range(len(labels))])
            with open('record.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                for row in rows:
                    writer.writerow(row)

            csvFile.close()
            cv2.destroyWindow("out")
        # cv2.waitKey(100)
