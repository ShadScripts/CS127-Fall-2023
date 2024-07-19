#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: Sepetember 12, 2023
#This program creates a blue smear!

import turtle

turtle.colormode(255)
shad = turtle.Turtle()
shad.shape("turtle")
shad.backward(100)

for i in range(0,255,10):
     shad.forward(10)
     shad.pensize(i)
     shad.color(0,0,i)