#its_not_python3 
import turtle
turtle.hideturtle()
turtle.speed(0)
def stam(x,y):
    turtle.begin_fill()
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.circle(10)
    turtle.end_fill()

def nth(x,y):
    turtle.begin_fill()
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.goto(x,y)
    turtle.goto(x+10,y)
    turtle.goto(x+10,y+10)
    turtle.goto(x,y)
    turtle.end_fill()
def color1():
    turtle.color("green")
turtle.getscreen().onkey(color1,"g")
turtle.getscreen().listen()
def color2():
    turtle.color("pink")
turtle.getscreen().onkey(color2,"p")
turtle.getscreen().listen()
def color3():
    turtle.color("brown")
turtle.getscreen().onkey(color3,"b")
turtle.getscreen().listen()
turtle.onscreenclick(stam,btn=1)
turtle.onscreenclick(nth,btn=3)
turtle.mainloop()

 
	
