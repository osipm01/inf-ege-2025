# Вперёд 3 Направо 270 Вперёд 5 Направо 90
#
# Опустить хвост
#
# Повтори 2 [Вперёд 10 Направо 270 Вперёд 12 Направо 270].

import turtle as t

t.lt(90)
size = 30
t.screensize(2000, 2000)
t.tracer(0)

t.down()

for _ in range(4):
    t.forward(10)
    t.right(270)

t.up()

t.forward(3)
t.right(270)
t.forward(5)
t.right(90)


for _ in range(2):
    t.forward(10)
    t.right(270)
    t.forward(12)
    t.right(270)

t.done()