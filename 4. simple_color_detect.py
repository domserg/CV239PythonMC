import cv2  # import OpenCV library

img = cv2.imread("girl.jpg", 1)  # read image 1-rgb, 0-greyscale, -1-rgba
cv2.imshow("image", img)  # show image

bgr_min = (100, 100, 30)
bgr_max = (220, 220, 100)
mask = cv2.inRange(img, bgr_min, bgr_max)
cv2.imshow("mask", mask)

cv2.waitKey(0)  # sleep
cv2.destroyAllWindows()  # destroy windows
