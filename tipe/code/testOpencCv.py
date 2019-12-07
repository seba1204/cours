import cv2
image = cv2.cv2.imread("clouds.jpg")
gray_image = cv2.cv2.cvtColor(image, cv2.cv2.COLOR_BAYER_BG2RGB(173,56,91))
cv2.cv2.imshow("Over the Clouds", image)
cv2.cv2.imshow("Over the Clouds - gray", gray_image)
cv2.cv2.waitKey(0)
cv2.cv2.destroyAllWindows()