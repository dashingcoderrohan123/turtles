#Write a program to draw a square inside a square?

import turtle

turtle.Screen().bgcolor("Yellow")
turtle.Screen().setup(300,300)

square=turtle.Turtle()

size=0


while True:
     for x in range(4):
          square.forward(size+1)
          square.left(90)
          size=size-5

     size=size+1

