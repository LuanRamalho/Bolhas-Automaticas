import random
from turtle import *
setup()

t = Turtle()

colors = ["blue", "red", "green", "purple", "yellow", "orange" , "cyan" , "pink" , "darkblue" , "olive"
          , "darkgreen" , "magenta" , "gold"]

t.up()
t.speed(0)

while True:

 x = random.randint(-300, 300)
 y = random.randint(-300, 300)
 circle_size = random.randint(1, 300)
 circle_color = random.choice(colors)
 t.goto(x, y)
 t.down()
 t.color(circle_color)
 t.begin_fill()
 t.circle(circle_size)
 t.end_fill()
 t.up()