#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: September 21, 2023
#This program makes a string pyramid!

s = input("")
ls = len(s)
for i in range(1,ls+1,1):
    print(s[:i])
for i in range(ls):
    print(s[i:])
print("Done!")