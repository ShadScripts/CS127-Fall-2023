#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: September 28, 2023
#This program tells me amount of snow pixels!

import matplotlib.pyplot as plt

s = input("Give filename")
t = 0.75
snow_count = 0
s = plt.imread(s)

for i in range(s.shape[0]):
    for j in range(s.shape[1]):
        if (s[i,j,0] > t) and (s[i,j,1] > t) and (s[i,j,2] > t): #check all colors per pixel
             snow_count += 1
print(f"Snow count is {snow_count}")