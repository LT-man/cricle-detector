import cv2
ghost = cv2.imread("dots.jpg")
gray = cv2.cvtColor(ghost, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0,0)
cv2.imshow("screen", blur)
cv2.waitKey(0)

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 10, param1 = 190, param2 = 50, minRadius = 3, maxRadius = 60)
print(circles[0,0:20])
for point in circles[0,:]: 
    x, y, r = int(point[0]), int(point[1]), int(point[2])
    cv2.circle(ghost, (x, y), r, (23, 78, 1), 10)
    cv2.imshow("screen2", ghost)
    cv2.waitKey(0)