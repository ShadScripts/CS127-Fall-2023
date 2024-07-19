#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: Oct 27, 2023
#This program gives a greeting based on time!

time = int(input("What time is it. "))

if time < 12:
    print("Good Morning")
elif time > 12 and time < 17:
    print("Good Afternoon")
else:
    print("Good evening")