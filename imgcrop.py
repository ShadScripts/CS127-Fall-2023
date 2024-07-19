#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: October 20, 2023
#This program crops the bottom left corner of the img!


import matplotlib.pyplot as plt

inF = input("Enter file name: ")
finalfile = input("Enter output file name")
img = plt.imread(inF)

height = img.shape[0]
width = img.shape[1]

img2 = img[height//2:, :width//2]

plt.imsave(finalfile, img2)