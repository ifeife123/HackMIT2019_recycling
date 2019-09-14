'''
file to deal wth webcam actions including:
 - live camera feed
 - picture taking
'''

# code take from
# https://stackoverflow.com/questions/21523398/how-to-give-start-stop-capture-and-close-buttons
# -in-opencv-cam-window-in-pytho
import cv2

run = True
path = 0


def listener(event):
    global run
    # check which mouse button was pressed
    # e.g. take picture on left mouse click
    if event == cv2.EVENT_LBUTTONDOWN and run:
        run = False

    run = True
    return

window_name = 'videoPlayer'
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, listener)

cap = cv2.VideoCapture(path)
while run:
    success, frame = cap.read()
    cv2.imshow(window_name, frame)
    cv2.waitKey(10)
