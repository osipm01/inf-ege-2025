import turtle as t

t.lt(90)
t.screensize(700, 700)
t.tracer(0)
size = 30

t.down()

for _ in range(0, 9):
    t.forward(22 * size)
    t.right(90)
    t.forward(6 * size)
    t.right(90)

t.up()

t.forward(1 * size)
t.right(90)
t.forward(75 * size)
t.left(90)

t.down()

for _ in  range(0, 9):
    t.forward(53 * size)
    t.right(90)
    t.forward(75 * size)
    t.right(90)

for x in range(-20, 20):
    for y in range(-20, 20):
        t.setpos(x * size, y * size)
        t.dot(10, 'red')

t.done()