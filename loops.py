#i is an incrementor/iterator
import turtle
from turtle import *
t = Turtle()


t.shape('turtle')
t.speed(10)

#def shape():
#    for i in range(4):
#        t.forward(125)
 #   t.left(90)


#def equal(x):
#    for i in range(3):
#        t.forward(x)
#        t.left(120)
#equal(100)

""" def square():
    for i in range(60):
        for i in range (4):
            t.forward(100)
            t.left(90)
        t.right(5)
square()
 """

""" def square(lenght):
    lenght=5
    for i in range(60):
        for i in range (4):
            t.forward(lenght)
            t.left(90)
        lenght = lenght + (5)
        t.right(5)
square(5) """

def star(lenght):
    lenght=7
    for i in range(60):
        for i in range (5):
            t.forward(lenght)
            t.left(144)
        lenght = lenght + (5)
        t.right(5)
star(5)


turtle.done()
