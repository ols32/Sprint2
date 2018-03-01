#Installa turtle
import turtle
import os

#Búum til leikmann
player = turtle.Turtle()
player.color("purple")
player.shape("circle")
player.shape("image", pig.gif)

#Borð 1
#Bakgrunnur:
wn=turtle.Screen()
wn.bgcolor("yellow") #fyrir stráborð
player.penup() #höfum pennan uppi svo við drögum ekki línu allt sem hann fer
player.speed(0) #hraði eins hratt og mögulegt er
player.setposition(-230,0) #Byrjunarstaða
player.setheading(90)

#Draw border
border_pen=turtle.Turtle()
border_pen.speed(0) #hraði 0 er hraðastur
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-250,-250)
border_pen.pendown()
border_pen.pensize()
#teiknum kassa sem border
for side in range(4):
    border_pen.fd(500)
    border_pen.lt(90)
border_pen.hideturtle()
line_pen=turtle.Turtle()
line_pen.speed(0)
line_pen.color("black")
line_pen.penup()
line_pen.setposition(-250,20)
line_pen.pendown()
line_pen.pensize()
for side in range (1):
    line_pen.fd(100)
    line_pen.lt(90)
    line_pen.fd(100)
    line_pen.lt(270)
    line_pen.fd(100)
    line_pen.lt(270)
    line_pen.fd(200)
    line_pen.lt(90)
    line_pen.fd(200)
    line_pen.lt(90)
    line_pen.fd(70)
    line_pen.lt(270)
    line_pen.fd(100)
line2_pen=turtle.Turtle()
line2_pen.speed(0)
line2_pen.color("black")
line2_pen.penup()
line2_pen.setposition(-250,-20)
line2_pen.pendown()
line2_pen.pensize()
for side in range (1):
    line2_pen.fd(140)
    line2_pen.lt(90)
    line2_pen.fd(100)
    line2_pen.lt(270)
    line2_pen.fd(20)
    line2_pen.lt(270)
    line2_pen.fd(200)
    line2_pen.lt(90)
    line2_pen.fd(280)
    line2_pen.lt(90)
    line2_pen.fd(50)
    line2_pen.lt(270)
    line2_pen.fd(60)
#Hraði leikmanns
playerspeed = 20
#Setjum upp hreyfingar fyrir leikmanninn
#Gerum það þannig að leikmaðurinn komist ekki út fyrir ramma borðsins
#Hreyfing til vinstri
def move_left():
    x=player.xcor() #x verður núverandi staða leikmanns
    x-=playerspeed
    if x<-230:
        x=-230
    player.setx(x)
#Hreyfing til hægri
def move_right():
    x=player.xcor()
    x +=playerspeed
    if x>230:
        x=230
    player.setx(x)

def move_up():
    y=player.ycor()
    y+=playerspeed
    if y>230:
        y=230
    player.sety(y)

def move_down():
    y=player.ycor()
    y-=playerspeed
    if y<-230:
        y=-230
    player.sety(y)
#Ef við viljum að leikmaðurinn geti aukið hraðann
#def increaseplayerspeed():
    #global playerspeed
    #playerspeed += 1

#Tengjum hreyfingar við lyklaborð
wn.listen()
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
#Til að leikmaður geti aukið hraðann, þarf eitthvað annað en Enter
#wn.onkey(increaseplayerspeed, "BUTTON_SHIFT")

delay = input("Halló")
wn.mainloop()
