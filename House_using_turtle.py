from turtle import *

wn = Screen()
wn.bgcolor("black")

afridi = Turtle()
afridi.speed(1)

angle = 540/5
for i in range(5):
    afridi.forward(50)
    afridi.right(180-angle)
afridi.left(angle)
for i in range(4):
    afridi.forward(50)
    afridi.right(180-angle)
