import math
import turtle

s = turtle.Screen()
s.bgcolor("black")

pen = turtle.Turtle()
pen.speed(1)
pen.color("red")
pen.begin_fill()
pen.fillcolor('red')
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.setheading(60)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()
s.mainloop()




