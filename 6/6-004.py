
# Повтори 2 [
#   Вперёд 3*x Направо 90 
#   Вперёд x Направо 90 
#   Повтори 2 [ Вперёд x Налево 90 ]
#   Повтори 2 [ Вперёд x Направо 90 ]
#   ]

from turtle import *

screensize(1000, 1000)
tracer(False)
size = 30

x = 5

down()

for _ in range(2):
    forward(x * size * 3)
    right(90)
    forward(x * size)
    right(90)
    for _ in range(2):
        forward(x * size)
        left(90)

    for _ in range(2):
        forward(x * size)
        right(90)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * size, y * size)
        dot(3, "red")

done()