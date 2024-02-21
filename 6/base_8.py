from turtle import *


shape('turtle')
color('green')
screensize(4000, 4000)
speed(100)
tracer(0)  # опасная команда

left(90)
k = 20
x=0
y=0
# up()
for i in range(7):
    x += 6
    y -= 9
    goto(x * k, y * k)
    dot(5, 'red')
    x -= 6
    y += 2
    goto(x * k, y * k)
    dot(5, 'red')
    x += 12
    y += 3
    goto(x * k, y * k)
    dot(5, 'red')


# рисуем точки
up()
for x in range(40):
    for y in range(-20, 2):
        goto(x * k, y * k)
        dot(5, 'red')
done()