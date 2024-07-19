#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: November 2, 2023
#This makes a turtle walk 100 times in random directions!

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(0,359)
  trey.right(a)
