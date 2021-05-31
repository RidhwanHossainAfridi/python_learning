from turtle import *

wn = Screen()
primeturtle = Turtle()
primeturtle.pensize(0.1)
primeturtle.up()

lower = 2
upper = 2000
primelist = []

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primelist.append(num)
for i in primelist:
    primeturtle.forward(i/20)
    primeturtle.right(36)
    primeturtle.stamp()
wn.exitonclick()



