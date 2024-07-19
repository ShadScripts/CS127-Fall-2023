#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: August 31st, 2023
#This program orginizes names!

list = input("Give me the names. ")
names = list.split("; ")
for name in names:
    final = name.split(", ")
    print(final[1],final[0])
