#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: September 7, 2023
#This program makes purple bridges!

import matplotlib.pyplot as plt
import numpy as np


img = plt.imread('csBridge.png')   #Read in image from csBridge.png
plt.imshow(img)		                 #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,1] = 0          #Set the green channel to 0

plt.imshow(img2)         #Load our new image into pyplot
plt.show()               #Show the image (waits until closed to continue)

plt.imsave('reds.png', img2)  #Save the image we created to the file: reds.png