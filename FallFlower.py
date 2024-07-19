#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: August 31st, 2023
#This program creates a flower!

import matplotlib.pyplot as plt


img = plt.imread('csBridge.png')

height = img.shape[0]
length = img.shape[1]

img2 = img[height//2:,:length//2]

plt.imshow(img2)
plt.show()