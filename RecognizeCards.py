import cv2

image_color = cv2.imread("Photos\korol-chervey.jpg")
image = cv2.imread("Photos\korol-chervey.jpg", cv2.IMREAD_GRAYSCALE)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold = 230
image[image > threshold] = 255
image[image < threshold] = 0

for i in range(50, 100):
    for j in range(100, 300):
        image_color[i, j] = [255, 0, 0]

cv2.imshow("card", image_color)
cv2.waitKey(0)
cv2.destroyAllWindows()






# cap = cv2.VideoCapture(0)

# while True:
#     ret, image = cap.read()
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     gray_image[gray_image > threshold] = 255
#     gray_image[gray_image < threshold] = 0
#     cv2.imshow("camera", gray_image)
#     if cv2.waitKey(10) == 27:
#         break
# cap.release()
#cv2.waitKey(0)


