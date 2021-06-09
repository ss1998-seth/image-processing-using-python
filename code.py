🔅 Task 4.1

📌 Create image by yourself Using Python Code 

import cv2

cn=numpy.zeros((500,500,3))
cv2.imshow('hi',cn)
cv2.waitKey()
cv2.destroyAllWindows()
cn = np.zeros((500,500, 3), dtype=np.uint8)
cn[100:400,100:120]=[181,101,29]
cn[100:125,120:300]=[244,196,48]
cn[125:150,120:300]=[255,255,255]
cn[150:175,120:300]=[0,255,0]
img = Image.fromarray(cn, 'RGB')
img.save('my.png')
img.show()


🔅 Task 4.2

📌 Take 2 image crop some part of both image and swap it. 

pic1= cv2.imread('img1.jpg')
pic1=cv2.resize(pic1,(1000,750))
cv2.imshow('one',pic1)
cv2.waitKey()
cv2.destroyAllWindows()
pic1.shape

crop1=pic1[200:380,370:550]
cv2.imshow('one',crop1)
cv2.waitKey()
cv2.destroyAllWindows()
pic2= cv2.imread('img2.jpg')
cv2.imshow('one',pic2)
cv2.waitKey()
cv2.destroyAllWindows()
pic2.shape

crop2=pic2[200:380,370:550]
cv2.imshow('one',crop2)
cv2.waitKey()
cv2.destroyAllWindows()

pic2[200:380,370:550]= crop1
cv2.imshow('one',pic2)
cv2.waitKey()
cv2.destroyAllWindows()

pic1[200:380,370:550]= crop2
cv2.imshow('one',pic1)
cv2.waitKey()
cv2.destroyAllWindows()


🔅 Task 4.3

📌 Take 2 image and combine it to form single image. For example collage 

pic1= cv2.imread('img1.jpg')
pic1=cv2.resize(pic1,(1000,750))
cv2.imshow('one',pic1)
cv2.waitKey()
cv2.destroyAllWindows()

pic2= cv2.imread('img2.jpg')
cv2.imshow('one',pic2)
cv2.waitKey()
cv2.destroyAllWindows()

img=np.hstack((pic1,pic2))
cv2.imshow('one',img)
cv2.waitKey()
cv2.destroyAllWindows()
