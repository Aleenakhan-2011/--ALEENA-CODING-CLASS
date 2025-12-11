import turtle

#creating canvas
turtle.Screen().bgcolor("lightblue")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

pen= turtle.Turtle()
angle = 360 / 4

for i in range(4):  
    pen.forward(100)
    pen.left(angle)

turtle.done()