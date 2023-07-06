import cv2  # import OpenCV library

img = cv2.imread("girl.jpg", 1)  # read image 1-rgb, 0-greyscale, -1-rgba
cv2.imshow("original image", img)  # show image

cv2.circle(img, (40, 80), 4, (0, 0, 255), -1)
cv2.rectangle(img, (60, 100), (120, 200), (255, 0, 0), 3)
cv2.line(img, (10, 20), (100, 50), (0, 255, 0), 3)
# текст добавьте сами
cv2.imshow("image", img)

cv2.waitKey(0)  # sleep
cv2.destroyAllWindows()  # destroy windows
