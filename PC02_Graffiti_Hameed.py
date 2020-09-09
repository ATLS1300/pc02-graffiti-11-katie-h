#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Katie Hameed
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
up()
goto(-20,95)
width(3)
down()
circle(20)
up()
goto(95,-75)
width(1)
left(75)
down()
forward(50)
backward(20)
left(45)
forward(20)
backward(20)
right(90)
forward(20)
backward(20)
left(45)
forward(20)
up()
right(45)
forward(10)
down()
circle(15)
up()
goto(90,-95)
left(45)
left(180)
down()
forward(15)
left(45)
forward(20)
backward(20)
right(90)
forward(20)
up()
goto(300,100)
right(30)
down()
width(5)
forward(200)
right(90)
forward(100)
right(90)
forward(200)
right(90)
forward(100)
up()
goto(225,150)
right(180)
down()
begin_fill()
circle(25)
end_fill()






