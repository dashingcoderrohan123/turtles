#Write a program to draw a star using a turtle?

import turtle

turtle.Screen().bgcolor("Blue")
turtle.Screen().setup(400,400)


star=turtle.Turtle()

star.forward(100)
star.left(120)
star.forward(100)
star.left(120)
star.forward(100)

star.penup()
star.right(150)  
star.forward(50)
star.pendown()

star.right(90)

star.forward(100)
star.right(120)
star.forward(100)
star.right(120)
star.forward(100)

turtle.done()