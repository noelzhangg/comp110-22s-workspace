from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(-150, -100)
leo.pendown()

colormode(255)
leo.pencolor(88, 24, 69)
leo.fillcolor(144, 12, 63)

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()


bob: Turtle = Turtle()

colormode(255)
bob.pencolor(0, 0, 0)

bob.penup()
bob.goto(-150, -100)
bob.pendown()

side_length: float = 300
i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
    side_length = side_length * 0.97

done()