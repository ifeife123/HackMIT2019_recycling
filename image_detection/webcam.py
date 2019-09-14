'''
file to deal wth webcam actions including:
 - live camera feed
 - picture taking
'''

import cv2


class WebCam:
    def __init__(self, window_name='videoPlayer'):
        self.is_taking_picture = False
        self.path = 0
        self.window_name = window_name
        self.imageFileQueue = []
        self.imageIndex = 0
        self.run = True
        self.cam_setup()
        self.start_recording()

    def clear_queue(self):
        """
        clears the imageFileQueue
        :return:
        """
        self.imageFileQueue = []

    def picture_taker(self, capture_object, number_of_pictures=1, wait_time=100):
        """
        saves frames to frames folder
        :param capture_object:
        :param number_of_pictures:
        :param wait_time:
        :return:
        """
        images = []

        for i in range(number_of_pictures):
            success, frame = capture_object.read()
            images.append(frame)
            cv2.waitKey(wait_time)
        for i, image in enumerate(images):
            print("saving image to frames/frame%d.jpg" % self.imageIndex)
            cv2.imwrite("frames/frame%d.jpg" % self.imageIndex, image)
            self.imageFileQueue.append("frames/frame%d.jpg" % self.imageIndex)
            self.imageIndex += 1
            print(self.imageFileQueue)
        return

    def cam_setup(self):
        def listener(event, x, y, flags, param):
            # take picture on left mouse click
            if event == cv2.EVENT_LBUTTONDOWN and not self.is_taking_picture:
                self.run = False
                self.is_taking_picture = True
                self.picture_taker(self.cap)
            self.is_taking_picture = False
            return

        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, listener)

        self.cap = cv2.VideoCapture(self.path)

    def display_result(self, imgfile):
        cv2.imshow(self.window_name, imgfile)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def start_recording(self):
        self.run = True
        while self.run:
            success, frame = self.cap.read()
            cv2.imshow(self.window_name, frame)
            cv2.waitKey(10)
        cv2.destroyAllWindows()

# test = WebCam()
