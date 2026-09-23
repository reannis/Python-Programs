'''
 Name:Russell Annis
 Date:September 23, 2020
 Course Number: csc-113-D03
 Course Name: intro to python programing
 Problem Number: 2
 Email: reannis2501@student.stcc.edu
 Problem Description: draw a house using turtle graphics
'''
import turtle
turtle.Screen().bgcolor("sky blue")
t = turtle.Turtle()
t.speed(100)

t.penup()
t.goto(-90, 50)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.end_fill()
t.penup()
t.forward(-30)
t.right(90)
t.forward(30)
t.pendown()

t.fillcolor("white")
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.end_fill()

t.penup()

t.forward(90)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.end_fill()

t.penup()
t.right(90)

t.forward(60)
t.right(90)
t.forward(-5)
t.left(90)

t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.end_fill()

t.penup()
t.goto(-90, 50)
t.left(50)
t.pendown()
t.fillcolor("maroon")
t.begin_fill()
t.forward(160)
t.right(102.5)
t.forward(155)
t.right(127.5)
t.forward(200)
t.end_fill()

t.penup()
t.hideturtle()
