#importing the computer vision library
import cv2

#to check the version of opencv
print(cv2.__version__)

#using the pre-trained classifier from OpenCV
#keep the xml file in the same folder as the code file
face_cascade=cv2.CascadeClassifier('face_detector.xml')

#upload and read the input image
img=cv2.imread('test.jpg')

#perform face detection
face=face_cascade.detectMultiScale(img,1.1,4) #to detect the face on the image

#draw rectangle around the face(enclose the face)
for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

#export the result(image with face detected)
cv2.imwrite('detected_face.jpg',img)
print('Result generated successfully!')


