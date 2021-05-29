#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import random


# In[ ]:


wn = turtle.Screen()
wn.bgcolor("black")
astroid = turtle.Turtle()
astroid.speed(0)
triad = turtle.Turtle()
triad.speed(0)
triad.up()
triad.goto(-140, 140)
triad.down()
squad = turtle.Turtle()
squad.speed(0)
squad.up()
squad.goto(140, 140)
squad.down()
pentago = turtle.Turtle()
pentago.speed(0)
pentago.up()
pentago.goto(-140, -140)
pentago.down()
octago = turtle.Turtle()
octago.speed(0)
octago.up()
octago.goto(140, -140)
octago.down()
colors = ["red", "gold", "blue", "green", "white", "cyan", "silver"]

for i in range(50):
    triad.color(random.choice(colors))
    triad.forward(i * 3)
    triad.left(120)

for i in range(50):
    squad.color(random.choice(colors))
    squad.forward(i * 2)
    squad.left(90)

for i in range(50):
    pentago.color(random.choice(colors))
    pentago.forward(i * 2)
    pentago.left(72)

for i in range(75):
    octago.color(random.choice(colors))
    octago.forward(i)
    octago.left(60)

for i in range(50):
    astroid.color(random.choice(colors))
    astroid.forward(i * 3)
    astroid.left(144)

triad.up()
triad.goto(-110, 200)
triad.down()
triad.write("PYTHON")
triad.hideturtle()

squad.up()
squad.goto(120, 200)
squad.down()
squad.write("LANGUAGE")
squad.hideturtle()

pentago.up()
pentago.goto(-140, -20)
pentago.write("ORIGINATES")
pentago.hideturtle()

octago.up()
octago.goto(120, -40)
octago.down()
octago.write("1991 ")
octago.hideturtle()

astroid.up()
astroid.goto(0, 60)
astroid.down()
astroid.write("IN")
astroid.hideturtle()

turtle.done()


# In[ ]:




