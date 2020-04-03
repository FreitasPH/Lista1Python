import turtle

def draw_square(t, sz):
    for i in range (4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Q1")
turtle = turtle.Turtle()
turtle.color("magenta")
turtle.pensize(3)
for i in range(5):
    draw_square(turtle, 20*(i+1))
    turtle.penup()
    turtle.setpos(-10*(i+1),-10*(i+1))
    turtle.pendown()
wn.mainloop()