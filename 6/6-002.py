import turtle as t

t.lt(90)
size = 30
t.screensize(500, 500)
t.tracer(0)

t.down()

for _ in range(4):
    for _ in range(4):
        t.forward(6 * size)
        t.right(90)
    t.forward(size * 10)
    t.right(90)
    t.forward(size * 3)

t.up()

for x in range(-20, 20):
    for y in range(-20, 20):
        t.setpos(x * size, y * size)
        t.dot(4, 'red')

t.done()