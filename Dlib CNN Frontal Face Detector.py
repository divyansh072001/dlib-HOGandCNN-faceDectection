import cv2
import dlib
import time

img1 = cv2.imread("media/group photo.jpg")
# img1 = cv2.imread("media/queue people.jpg")

cnn_face_detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")

start_time = time.time()

faces_cnn = cnn_face_detector(img1, 1)

end_time = time.time()
total_time = end_time-start_time

print("\n Time taken for CNN face detection: ", total_time)

for face in faces_cnn:
    x = face.rect.left()
    y = face.rect.top()
    w = face.rect.right() - x
    h = face.rect.bottom() - y

    cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 0), 2)

img_height, img_width = img1.shape[:2]
cv2.putText(img1, "CNN", (img_width-50, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# display output image
cv2.imshow("face detection with dlib", img1)
cv2.waitKey()

# save output image
cv2.imwrite("cnn_face_detection.png", img1)

# close all windows
cv2.destroyAllWindows()
