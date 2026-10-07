import turtle
from turtle import *
t = Turtle()


t.shape('turtle')

def rectangle(x=100):
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(125)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(125)
rectangle(100)

def equal():
    turtle.forward(125)
    turtle.left(120)
    turtle.forward(125)
    turtle.left(120)
    turtle.forward(125)
    turtle.left(120)
equal()

def message(input):
    print(input)
message("I am a strange turtle")

turtle.done()