import turtle

##turtle.bgcolor("black")
##turtle.pensize(2)
##turtle.speed(0)
##
##for i in range(6):
##    for colours in ["red","magenta","cyan","green","yellow","white"]:
##        turtle.color(colours)
##        turtle.circle(100)
##        turtle.left(10)
##turtle.hideturtle()    


t = turtle.pensize(4)
turtle.bgcolor("black")
turtle.speed(0)
for x in range(30):
    for colours in ["red","purple","blue","green","yellow","orange"]:
        
        turtle.color(colours)
        turtle.triangle(100)
        turtle.left(10)
turtle.hideturtle()
