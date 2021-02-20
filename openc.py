'''
import cv2
#img=cv2.imread("/root/Downloads/Elon-Musk-PowerPoint-Template-Preview.jpg",1) #Color img
img= cv2.imread("/root/Downloads/Elon-Musk-PowerPoint-Template-Preview.jpg",0)  #Greyscale img
#print(img)
print(type(img))
print(img.shape)

#Resize
#resized =cv2.resize(img,(400,400))
resized =cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
#resized =cv2.resize(img,(int(img.shape[1]*2),int(img.shape[0]*2)))
                    
cv2.imshow("Elon-Musk-PowerPoint-Template-Preview.jpg", resized)

#cv2.waitKey(0)
cv2.waitKey(2000)
cv2.destroyAllWindows()
'''

#Face   Detection******************
import cv2

#create a   cascadeClassifier Object
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

#Reading the image as it is
img=cv2.imread("/root/Downloads/Elon-Musk-PowerPoint-Template-Preview.jpg")

#Reading the image as Gray  scale
gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Searching the co-ordinates
faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,
                                    minNeighbors=5)
for x,y,w,h in faces:
    img= cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,0),3)
resized =cv2.resize(img,(int(img.shape[1]/7),int(img.shape[0]/7)))
cv2.imshow("Gray",resized)#img/resized

cv2.waitKey(0)

cv2.destroyAllWindows()
