import cv2,glob
 
all_images=glob.glob("*.png")
detect=cv2.CascadeClassifier("haarcascade_frontalface_default (1).xml")

for image in all_images:
    img=cv2.imread(image)
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=detect.detectMultiScale(gray_img,1.1,5)
    
    for(x,y,w,h) in faces:
        final_img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow("group photo",final_img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows() 