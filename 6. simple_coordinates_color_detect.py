import cv2  # import OpenCV library

img = cv2.imread("girl.jpg", 1)  # read image 1-rgb, 0-greyscale, -1-rgba
cv2.imshow("image", img)  # show image
bgr_min = (100, 100, 30)
bgr_max = (220, 220, 100)
mask = cv2.inRange(img, bgr_min, bgr_max)
cv2.imshow("mask", mask)

obj = cv2.moments(mask)
cXo = int(obj['m10'] / obj['m00'])
cYo = int(obj['m01'] / obj['m00'])

cv2.circle(img, (cXo, cYo), 20, (255, 0, 0), 5)
cv2.imshow("image", img)
cv2.waitKey(0)  # sleep
cv2.destroyAllWindows()  # destroy windows
