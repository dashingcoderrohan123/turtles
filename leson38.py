#Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle?

import turtle#importing the lirary

turtle.Screen().bgcolor("Red")#giving bg color
turtle.Screen().setup(400,400)#giving screen size


polygon=turtle.Turtle()

num_side=6
side_length=70
angle=360.0/6

for x in range(num_side):
    polygon.forward(side_length)
    polygon.right(angle)


turtle.done()
    