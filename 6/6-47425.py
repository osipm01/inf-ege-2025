import turtle as t

t.lt(90)
size = 30
t.screensize(2000, 2000)
t.tracer(0)

t.down()

for _ in range(5):
    t.fd(9 * size)
    t.rt(120)

t.up()

for x in range(-20, 20):
    for y in range(-20, 20):
        t.setpos(x * size, y * size)
        t.dot(4, 'red')

t.done()