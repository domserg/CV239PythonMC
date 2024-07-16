import cv2  # import OpenCV library

id = 0
cap = cv2.VideoCapture(id)
hsv_min = (100, 100, 30)
hsv_max = (179, 255, 255)
key = -1
while (key != 27):
    ret, frame = cap.read()
    if ret:  # Display the resulting frame
        cv2.imshow('Frame', frame)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, hsv_min, hsv_max)
        cv2.imshow("Mask", mask)
        m = cv2.moments(mask)
        mc = int(m['m10'] / (m['m00'] + 1)), int(m['m01'] / (m['m00'] + 1))
        cv2.circle(frame, mc, 20, (255, 0, 0), 2)
        cv2.imshow("Frame with mc", frame)
    # When everything done, release the video capture object
    key = cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()  # destroy windows
