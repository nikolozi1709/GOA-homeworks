from turtle import *
#walls
speed(100)
color("blue")
begin_fill()
width(5)
forward(200)
left (90)
forward(200)
left(90)
forward(200)
color()
left (90)
forward(200)
left(90)
end_fill()
# door
forward(70)
color("red")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
#roof
penup()
goto(200, 200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window 
color("purple")
penup()
goto(10,110)
left(120)
pendown()
forward(50)
left(90)
forward(25)
left(90)
forward(50)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
# second window
penup()
goto(130,110)
pendown()
left(90)
forward(25)
left(90)
forward(50)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
exitonclick ()




