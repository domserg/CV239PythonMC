import cv2  # import OpenCV library

id = 0
cap = cv2.VideoCapture(id)
key = -1
while (key != 32):
    ret, frame = cap.read()
    if ret == True:  # Display the resulting frame
        cv2.imshow('Frame', frame)
    # When everything done, release the video capture object
    key = cv2.waitKey(25)
cap.release()
cv2.destroyAllWindows()  # destroy windows
