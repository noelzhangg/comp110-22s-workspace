"""Draw a smiley face using Turtle. Breakdown of tast of drawing a tongue into the tongue itself and then the tongue line in a separate function: lines 75 - 101."""

__author__ = "730490949"

from turtle import Turtle, colormode, done 

speedy: Turtle = Turtle()
speedy.hideturtle()

speedy.speed(70)


# main function to call function and draw complete smiley face
def main() -> None:
    """The entrypoint of my scene."""
    draw_smiley_head(speedy, -150, -100)
    draw_smiley_eye(speedy, -55, 100)
    draw_smiley_eye(speedy, 40, 100)
    draw_smiley_mouth(speedy, -90, 70)
    draw_smiley_tongue(speedy, 50, -30)
    draw_smiley_tongue_line(speedy, 58, -30)
    done()


# smiley face head
def draw_smiley_head(speedy: Turtle, x: float, y: float) -> None:
    """Drawing the smiley face square head."""
    speedy.penup()
    speedy.goto(x, y)
    speedy.setheading(0.0)
    speedy.pendown()
    colormode(255)
    speedy.pencolor(0, 0, 0)
    speedy.fillcolor(250, 213, 3)
    speedy.begin_fill()
    i: int = 0
    while i < 4:
        speedy.forward(300)
        speedy.left(90)
        i = i + 1
    speedy.end_fill()


# smiley face eye
def draw_smiley_eye(speedy: Turtle, x: float, y: float) -> None:
    """Drawing the square eye."""
    speedy.penup()
    speedy.goto(x, y)
    speedy.pendown()
    speedy.color("black", "black")
    speedy.begin_fill()
    i = 0
    while i < 4:
        speedy.forward(10)
        speedy.left(90)
        i = i + 1
    speedy.end_fill()


# smiley face mouth
def draw_smiley_mouth(speedy: Turtle, x: float, y: float) -> None:
    """Drawing the smile mouth with lines."""
    speedy.penup()
    speedy.goto(x, y)
    speedy.setheading(270.0)
    speedy.pendown()
    speedy.pencolor("black")
    speedy.forward(100)
    speedy.left(90)
    speedy.forward(175)
    speedy.left(90)
    speedy.forward(100)


# smiley face tongue
def draw_smiley_tongue(speedy: Turtle, x: float, y: float) -> None:
    """Drawing a tongue sticking out of the smiley face mouth."""
    speedy.penup()
    speedy.goto(x, y)
    speedy.pendown()
    speedy.pencolor(251, 139, 227)
    speedy.fillcolor(251, 139, 227)
    speedy.setheading(270.0)
    speedy.begin_fill()
    speedy.forward(30)
    speedy.left(90)
    speedy.forward(15)
    speedy.left(90)
    speedy.forward(30)
    speedy.end_fill()


# tongue line function --> addition to drawing tongue function
def draw_smiley_tongue_line(speedy: Turtle, x: float, y: float) -> None:
    """Adding in a tongue line for dimension."""
    speedy.penup()
    speedy.goto(x, y)
    speedy.pendown()
    speedy.pencolor(205, 100, 183)
    speedy.setheading(270.0)
    speedy.forward(22)


if __name__ == "__main__":
    main()