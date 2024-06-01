# Turtle Graphics Practice Project

This project uses Python's `turtle` module to create a simple interactive program where you can control a turtle's movements on the screen using keyboard keys.

## Features

- **Move Forward**: Press `w` to move the turtle forward by 10 units.
- **Move Backward**: Press `s` to move the turtle backward by 10 units.
- **Turn Left**: Press `a` to turn the turtle left by 20 degrees.
- **Turn Right**: Press `d` to turn the turtle right by 20 degrees.
- **Clear Screen**: Press `c` to clear the screen and reset the turtle.

## Code

```python
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
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backforward)
    screen.onkey(key="a", fun=move_left)
    screen.onkey(key="d", fun=move_right)
    screen.onkey(key="c", fun=clear)

setup_keys()
screen.listen()
screen.exitonclick()
