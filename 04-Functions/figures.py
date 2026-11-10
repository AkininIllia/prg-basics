import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)

def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

def draw_rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)