#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: September 7, 2023
#This program makes left turns!

import turtle
shad = turtle.Turtle()

def method():
    number = input("Give me a number: ")
    return number

a = method()
b = method()
c = method()
d = method()
e = method()
values = [a,b,c,d,e]
for i in range(5):
    shad.forward(100)
    shad.left((values[i]))