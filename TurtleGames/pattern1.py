import turtle

t = turtle.Turtle()

for c in ['black','blue','green']:
  for i in range(25):
    t.color(c)
    t.forward(75)
    t.left(91.2)
  t.up()
  t.forward(150)
  t.down()