#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: October 30, 2023
#This program makes a complex triangle!

def triangle(t, length):
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
        triangle(t, length/2)

def  nestedTriangle(t, length):
    if length > 10:
        for x in range(3):
            t.forward(length)
            t.left(120)
            nestedTriangle(t, length/2)