from turtle import *


shape('turtle')
color('green')
screensize(4000, 4000)
speed(100)
tracer(0)  # опасная команда

left(90)

k = 40
for i in range(7):
    forward(10 * k)
    right(120)

# рисуем точки
up()
for x in range(10):
    for y in range(11):
        goto(x * k, y * k)
        dot(5, 'red')

forward(1000)
done()