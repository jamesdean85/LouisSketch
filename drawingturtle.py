from turtle import *
from itertools import cycle
from tkinter import *
from glob import glob
import turtle
import this


ts = turtle.getscreen()

ts.getcanvas().postscript(file="duck.eps")

jpgfiles = glob('*.jpg')
for u in jpgfiles:
    out = u.replace('jpg','eps')
    #print "Converting %s to %s" % (u, out)
    img=Image.read(u)
    img.save(out)


t=Turtle()


def saveImage():
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="imagesaved.eps")
    
def goto(x,y):
    t.goto(x,y)

def up():
    if not(t.heading() == 90):
        t.setheading(90)
        t.fd(20)
    else:
        t.fd(20)    
def down():
    if not(t.heading() == 270):
        t.setheading(270)
        t.fd(20)
    else:
        t.fd(20)    
def right():
    if not (t.heading() == 0):
        t.setheading(0)
        t.fd(20)
    else:
        t.fd(20)    
def left():
    if not (t.heading() ==180):
        t.setheading(180)
        t.fd(20)
    else:
        t.fd(20)
def undo_button():    
    t.undo()
    
def toggle_on_off():
    if not(t.pencolor() == ('black')):
        t.pencolor('black')
    else:
        t.pencolor('orange')
    

    
def clear():
    t.clear()
    
def hide_turtle_off():
    t.hideturtle()
    
def hide_turtle_on():
    t.showturtle()           

def pen_size_1():
    t.pensize(1)

def pen_size_2():
    t.pensize(2)
    
def pen_size_3():
    t.pensize(3)
    
def pen_size_4():
    t.pensize(4)
    
def pen_size_5():
    t.pensize(5)
    
def pen_size_6():
    t.pensize(6)
    
def pen_size_7():
    t.pensize(7)

def pen_size_8():
    t.pensize(8)

def pen_size_9():
    t.pensize(9)

def save():
    ts = t.getscreen()
    ts.getcanvas().postscript(file="drawing")
    
    
def place_picture():
    t.placescreen()
    
    
    

def color_cycle():
    t.pencolor(next(colors))

def undo_clear():
    t.undoclear()
    

    

    
def keyboard_commands():
    t.screen.onkey(up,"Up")
    t.screen.onkey(down,"Down")
    t.screen.onkey(right,"Right")
    t.screen.onkey(left,"Left")
    t.screen.onkey(up,"w")
    t.screen.onkey(down,"s")
    t.screen.onkey(right,"d")
    t.screen.onkey(left,"a")
    t.screen.onkey(undo_button,"End")
    t.screen.onkey(toggle_on_off,"e")
    t.screen.onkey(clear,'c')
    t.screen.onkey(hide_turtle_off,"z")
    t.screen.onkey(hide_turtle_on,"q")
    t.screen.onkey(color_cycle, "x")
    t.screen.onkey(undo_clear,'f')
    t.screen.onkey(pen_size_1,'1')
    t.screen.onkey(pen_size_2,'2')
    t.screen.onkey(pen_size_3,'3')
    t.screen.onkey(pen_size_4,'4')
    t.screen.onkey(pen_size_5,'5')
    t.screen.onkey(pen_size_6,'6')
    t.screen.onkey(pen_size_7,'7')
    t.screen.onkey(pen_size_8,'8')
    t.screen.onkey(pen_size_9,'9')
    t.screen.onkey(save,'k')
    t.screen.listen()

colors = cycle(["red", "orange", "yellow", "green", "blue", "indigo", "purple"])

t.screen.onclick(t.goto) #unfinished 
t.ondrag(goto)
t.screen.title("Louis' EtchaSketch")
t.screen.bgcolor("black")
t.color("orange")

keyboard_commands()
t.screen.mainloop()
