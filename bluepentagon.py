#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: Sepetember 12, 2023
#This program creates a pentagon of turtles!


import turtle
shad = turtle.Turtle()
shad.shape("turtle")
shad.color("cornflowerblue")

tot_rot = 360
sides = 5
for i in range(5):
    shad.stamp()
    shad.forward(100)
    shad.left(tot_rot/sides)

