#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#This program prints in simplified machine language!

wList = "Mon&Tues&Wednes&Thurs&Fri&Satur&Sun"
weeks = wList.split("&")
tgit = weeks[3]
print(tgit.upper())
print(weeks[-1])
for i in range(0,6,2):
    day = weeks[i]+"day"
    print(i,day)