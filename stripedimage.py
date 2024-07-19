#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: September 21, 2023
#This program makes a striped image!

import matplotlib.pyplot as plt
import numpy as np

size = int(input("How large do you want the image?: "))
img = np.ones((size, size, 3))
img[::,:,2] = 0.0 #yellow
img[::2,:,1:] = 0 #justred
img[::2,:,2:] = 1 #purple

plt.imsave('stripes.png', img)