import turtle
import figures

window = turtle.Screen()
window.bgcolor("lightgreen")

turtle.speed(3)

figures.draw_square(100)

turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
figures.draw_triangle(100)

turtle.penup()
turtle.goto(-100, 200)
turtle.pendown()
figures.draw_rectangle(100, 200)

turtle.hideturtle()
window.mainloop()
