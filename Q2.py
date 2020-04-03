import turtle
def draw_poly(t, n, sz):
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")    
    for i in range(n):
        t.forward(sz)
        t.left(360/n)
    wn.mainloop()

tess = turtle.Turtle()
tess.color("magenta")
tess.pensize(3)
draw_poly(tess, 8, 50)