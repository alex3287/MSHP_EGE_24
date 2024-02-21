from turtle import *


shape('turtle')
color('green')
screensize(4000, 4000)
speed(100)
tracer(0)  # опасная команда

left(90)

k = 20
for i in range(16):
    left(36)
    forward(4*k)
    left(36)
# рисуем точки
up()
for x in range(-6, 1):
    for y in range(-3, 4):
        goto(x * k, y * k)
        dot(5, 'red')

forward(40)
done()