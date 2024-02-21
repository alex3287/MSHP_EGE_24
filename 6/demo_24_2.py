from turtle import *


shape('turtle')
color('green')
screensize(4000, 4000)
speed(100)
tracer(0)  # опасная команда

left(90)

k = 30

for i in range(2):
    forward(8*k)
    right(90)
    forward(18*k)
    right(90)

up()
forward(4*k)
right(90)
forward(10*k)
left(90)

down()
for i in range(2):
    forward(17*k)
    right(90)
    forward(7*k)
    right(90)

# рисуем точки
up()
for x in range(19):
    for y in range(22):
        goto(x * k, y * k)
        dot(5, 'red')

print(19*22 - 11*13)
done()