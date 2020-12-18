#import library
import cv2 
import numpy as np

#add edge to the image function
def addEdge(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    #if the image is rgb the image is converted from rgb to gray
    if np.ndim(img) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    #define image size and edge size
    height=2400
    weight=2808
    edge_size = int((weight - img.shape[1])/2)

    #create edge
    edge = np.zeros((height, edge_size), np.uint8)

    #concanete edges and image 
    image = np.concatenate((edge,img,edge),axis=1)

    #return to refined image
    return image


#for loop to processing all image
for i in range(1,11):
    number = "00{}".format(i)
    if i >= 10:
        number = "0{}".format(i)

    #image path
    img_path = 'C://Users//halil//Desktop//opencv//xrayjpg//{}.jpg'.format(number)
    #image save path
    save_path = "C://Users//halil//Desktop//opencv//refined-xrayjpg//{}.jpg".format(number)

    #refined image
    image = addEdge(img_path)
    
    #Saved to refined image
    cv2.imwrite(save_path, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()