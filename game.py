import turtle
import random

window = turtle.Screen()
window.setup(1200 + 3, 800 + 3)
window.bgpic("images/Space.png")
window.screensize(1000, 600)


def airoplane(y):
    pen = turtle.Turtle()
    if y < 0:
        pen.color("orange")
    else:
        pen.color("red")
    for current_x in [-200, 0, 200]:
        pen.penup()
        pen.setpos(x=current_x, y=y)
        pen.pendown()
        pen.circle(radius=random.randint(50, 70))
        pen.forward(100)

airoplane(y=100)
airoplane(y=-100)

window.mainloop()

