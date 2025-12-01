
color = input('pick a color: ')

color.replace(" ", "_")

import turtle

pat = turtle.Turtle()

turtle.Screen().bgcolor("black")

pat.penup()

pat.forward(90)
pat.left(45)
pat.pendown()

pat.color(color)

def branch():
    for i in range(3):
        for i in range(3):
            pat.color()
            pat.forward(30)
            pat.backward(30)
            pat.right(45)
        pat.left(90)
        pat.backward(30)
        pat.left(45)
    pat.right(90)
    pat.forward(90)

for i in range(7):
    pat.color(color)
    branch()
    pat.left(45)
for i in range(3):
       for i in range(3):
           pat.color(color)
           pat.forward(30)
           pat.backward(30)
           pat.right(45)
       pat.left(90)
       pat.backward(30)
       pat.left(45)

pat.color('black')     
pat.penup()
pat.forward(1000)