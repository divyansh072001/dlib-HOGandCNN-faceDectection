import cv2
import dlib
import time

img1 = cv2.imread("media/group photo.jpg")
# img1 = cv2.imread("media/queue people.jpg")

hog_frontal_face = dlib.get_frontal_face_detector()

start_time = time.time()

faces_hog = hog_frontal_face(img1, 1)

end_time = time.time()
total_time = end_time-start_time

print("\n Time taken for HOG face detection: ",total_time)


for face in faces_hog:
    x = face.left()
    y = face.top()
    w = face.right() - x
    h = face.bottom() - y

    cv2.rectangle(img1,(x, y), (x+w,y+h), (0,0,255), 2)


img_height, img_width = img1.shape[:2]
cv2.putText(img1, "HOG", (img_width-50,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
# cv2.putText(img1, "CNN", (img_width-50,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

# display output image
cv2.imshow("face detection with dlib", img1)
cv2.waitKey()

# save output image
cv2.imwrite("hog_face_detection.png", img1)

# close all windows
cv2.destroyAllWindows()