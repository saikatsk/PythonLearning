import numpy as np
import cv2 as opencv
import time

print (":: My First Python Code ::")
print ("Hello world!")

def my_function():
    print ("Inside function: Hello world!")

my_function()
print ("Numpy is installed! Version: " + np.__version__)
print ("OpenCV is installed! Version: " + opencv.__version__)

'''
## Basics of Image Processing ##
# open an image, arguments <file name, color/greyscale/unchaged [1, 0, -1] >
img = opencv.imread("photo_with_white_background.jpg",1)

# create a show window, so that image is sized correctly
opencv.namedWindow('image', opencv.WINDOW_NORMAL)

# display an image arguments <image window name, image variable (used in read) >
opencv.imshow("image", img)
# wait for key press
opencv.waitKey(0)

# remove the image
opencv.destroyAllWindows()

# resize the image
resized_image = opencv.resize(img, (650,500))

# display an image arguments <image window name, image variable (used in read) >
opencv.imshow("image", resized_image)
# wait for key press
opencv.waitKey(0)

# remove the image
opencv.destroyAllWindows()
'''

'''
## Basics of Video Processing ##
video = opencv.VideoCapture("rtsp://admin:passwd@123@192.168.1.250:554")
check, frame = video.read()

#print(check)
#print(frame)

opencv.imshow("capture from video", frame)
opencv.waitKey(0)

#time.sleep(3)
video.release()
opencv.destroyAllWindows()
'''


# playing live video
video = opencv.VideoCapture("rtsp://admin:passwd@123@192.168.1.250:554")

capturedFrameCount = 1
while True:
    capturedFrameCount = capturedFrameCount + 1
    check, frame = video.read()
    opencv.imshow("capture from video", frame)
    key = opencv.waitKey(30)

    # press "q" to exit playback
    if key == ord('q'):
        break

print("Number of Captured Frames: " + str(capturedFrameCount))
video.release()
opencv.destroyAllWindows()
