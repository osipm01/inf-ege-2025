import turtle as t

t.lt(90)
size = 30
t.screensize(2000, 2000)
t.tracer(0)

t.down()

for _ in range(8):
    t.forward(size * 6)
    t.rt(120)

t.up()

for x in range(-20, 20):
    for y in range(-20, 20):
        t.setpos(x * size, y * size)
        t.dot(4, 'red')

t.done()