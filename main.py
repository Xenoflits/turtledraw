from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forward():
    t.forward(10)

def move_backforward():
    t.forward(-10)

def move_left():
    t.left(20)

def move_right():
    t.right(20)

def clear():
    global t
    screen.clearscreen()
    setup_keys()
    t = Turtle()

def setup_keys():
    screen.onkey(key="w",fun=move_forward)
    screen.onkey(key="s",fun=move_backforward)
    screen.onkey(key="a",fun=move_left)
    screen.onkey(key="d",fun=move_right)
    screen.onkey(key="c",fun=clear)

setup_keys()
screen.listen()
screen.exitonclick()
