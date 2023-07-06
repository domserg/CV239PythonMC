import cv2  # import OpenCV library

img = cv2.imread("girl.jpg", 1)  # read image 1-rgb, 0-greyscale, -1-rgba
cv2.imshow("image", img)  # show image
cv2.waitKey(0)  # sleep
cv2.destroyAllWindows()  # destroy windows
