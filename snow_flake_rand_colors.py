import turtle
import random

pat = turtle.Turtle()

turtle.Screen().bgcolor("black")

colors = ["cyan", "purple", "white", "blue", "yellow", "lime green", "orange"]

pat.penup()

pat.forward(90)
pat.left(45)
pat.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            pat.color(random.choice(colors))
            pat.forward(30)
            pat.backward(30)
            pat.right(45)
        pat.left(90)
        pat.backward(30)
        pat.left(45)
    pat.right(90)
    pat.forward(90)

for i in range(7):
    pat.color(random.choice(colors))
    branch()
    pat.left(45)
for i in range(3):
       for i in range(3):
           pat.color(random.choice(colors))
           pat.forward(30)
           pat.backward(30)
           pat.right(45)
       pat.left(90)
       pat.backward(30)
       pat.left(45)
       
       
pat.penup()
pat.color('black')
pat.forward(1000)
