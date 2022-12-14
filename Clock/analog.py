import time
import turtle
wndw = turtle.Screen()
wndw.bgcolor("black")
wndw.setup(width=600, height=500)
wndw.title("Analog Clock")
wndw.tracer(0)

# Create the drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(hr,mn,s,pen):
    # Draw clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)
    
    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle=(hr/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    pen.penup()
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90)
    angle=(mn/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

    pen.penup()
    pen.goto(0,0)
    pen.color("red")
    pen.setheading(90)
    angle=(s/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)

try:

    while True:
        hr=int(time.strftime("%I"))
        mn=int(time.strftime("%M"))
        s=int(time.strftime("%S"))
        draw_clock(hr,mn,s,pen)

        wndw.update()
        time.sleep(1)
        pen.clear()   

except:
    pass    


