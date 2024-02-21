from turtle import *


shape('turtle')
color('green')
speed(50)
tracer(0)  # опасная команда
screensize(4000, 4000)

left(90)

k = 60
for i in range(15):
    forward(15*k)
    right(120)

up()
for x in range(14):
    for y in range(16):
        goto(x*k, y*k)
        dot(5, 'red')

done()