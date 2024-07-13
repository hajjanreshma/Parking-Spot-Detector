# we are going to use image classifier and some mathematical techniques which are very commonly used in computer vision and
#
# opencv-python==4.6.0.66
# scikit-learn==1.1.3
# pandas==1.5.1
# Pillow==9.3.0
# scikit-image==0.17.2
# matplotlib==3.6.2
#
#
# we are not use complicated method
# yolo version 4 or 5
# or not using mobile net ssd to actually detect the car
# using the basic image processing to find whether the car is present or not
#
# In reality if we are doing it on a cctv camera then you don't expect it to move
# and u should have a fixed camera so in that case it should be fine
#
#
# pickles is the package that will be using to save all the places or the positions of
# the parking spaces and then bring it to our main code

# 1. AI Mouse:
# Project Title: AI-Powered Virtual Mouse
# Description: Developed a virtual mouse system using computer vision and machine learning
# to enable hands-free cursor control via hand gesture tracking.
#
# 2. Parking Spot Counter
# Project Title: Automated Parking Spot Counter
# Description: Created an image processing-based system to automatically detect and count available
# parking spots in real-time using machine learning models.
#
# 3. Virtual Canvas:
# Project Title: Interactive Virtual Canvas
# Description: Developed a virtual canvas application that tracks finger movements for drawing and writing,
# utilizing computer vision and gesture recognition with machine learning.





import cv2
import pickle
# img = cv2.imread('Parkingfiles/carParkImg.png')
width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarParkPos','wb') as f:
        pickle.dump(posList,f)



while True:
    # cv2.rectangle(img,(50,192),(157,240),(255,0,255),2)
    img = cv2.imread('Parkingfiles/carParkImg.png')
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image",mouseClick)
    cv2.waitKey(1)