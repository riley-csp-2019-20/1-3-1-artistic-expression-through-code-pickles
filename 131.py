import turtle as trtl
import time
#from playsound import playsound
#from threading import Thread
#def music():
    #playsound("https://ia800504.us.archive.org/33/items/TetrisThemeMusic/Tetris.mp3") #https://ia800608.us.archive.org/18/items/TheMoonTheme/The%20Moon%20Theme.mp3
#thread = Thread(target=music)
#thread.start()

#define variables
trondude1 = trtl.Turtle()
trondude2 = trtl.Turtle()
counter_interval = 1000   #1000 represents 1 second
timer1 = 1
timer2 = 1
timer1_up = False
timer2_up = False
speed1 = 4
speed2 = 4
#setup turtle and screen
trondude2.penup()
trondude2.goto(0,100)
trondude2.pendown()
trondude1.speed(3)
trondude2.speed(3)
trondude1.color("orange")
trondude2.color("green")
trondude1.setheading(0)
trondude2.setheading(0)
wn = trtl.Screen()
trondude1.xcor()
trondude1.ycor()
trondude2.xcor()
trondude2.ycor()

tron1Locations = []
tron2Locations = []
wn.bgcolor("black")


#head on collision
def collision(): 
    if (trondude1.xcor() >= trondude2.xcor()-5 and trondude1.xcor() <= trondude2.xcor()+5 and trondude1.ycor() >= trondude2.ycor()-5 and trondude1.ycor() <= trondude2.ycor()+5) :
        trondude1.color("white")
        trondude2.color("white")
        
#movement Tron1
def up():
    
    trondude1.forward(5)
def left():
    global counter
    trondude1.speed(0)
    trondude1.left(90)
    trondude1.speed(3)
def right(): 
    global counter
    trondude1.speed(0)
    trondude1.right(90)
    trondude1.speed(3)

#movement Tron2
def up2():
    trondude2.forward(5)

def left2():
    global counter
    trondude2.speed(0)
    trondude2.left(90)
    trondude2.speed(3)
def right2(): 
    global counter
    trondude2.speed(0)
    trondude2.right(90)
    trondude2.speed(3)

#restart game
def restart():
    global timer1, timer2, counter
    trondude1.clear()
    trondude2.clear()
    trondude1.penup()
    trondude2.penup()
    trondude1.goto(0,0)
    trondude2.goto(0,100)
    trondude1.setheading(0)
    trondude2.setheading(0)
    trondude1.pendown()
    trondude2.pendown()
    trondude1.speed(3)
    trondude2.speed(3)
    timer1 = 1
    timer2 = 1
    trondude1.color("orange")
    trondude2.color("green")
    tron1Locations.clear()
    tron2Locations.clear()

boostcounter1 = 0
boostcounter2 = 0

#Boost Tron 1
def boost1():
    
    global timer1, timer1_up, speed1
    if timer1 <= 0:
        timer1_up = True 
        speed1 = 4
    else:
        speed1 = 7
        timer1 -= 1
        trondude1.getscreen().ontimer(boost1, counter_interval) 
#Boost Tron 2 
def boost2():
    global timer2, timer2_up, speed2
    if timer2 <= 0:
        timer2_up = True 
        speed2 = 4
    else:
        speed2 = 7
        timer2 -= 1
        trondude2.getscreen().ontimer(boost2, counter_interval)         


#Key Press events
wn = trtl.Screen()

wn.onkeypress(boost1,"Up")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")

wn.onkeypress(boost2,"w")
wn.onkeypress(left2,"a")
wn.onkeypress(right2,"d")

wn.onkeypress(restart,"space")

wn.listen()
counter = 2
collision()
#line collision and turtle movement
while (True):
    trondude1.forward(speed1)
    trondude2.forward(speed2)
    
    
    if trondude2.pos() in tron1Locations or trondude2.pos() in tron2Locations:
        
        trondude2.color("white")
    if trondude1.pos() in tron2Locations or trondude1.pos() in tron1Locations:
        
        trondude1.color("white")

    tron1Locations.append(trondude1.pos())
    tron2Locations.append(trondude2.pos())
    collision()
    
    
wn.ontimer(countdown, counter_interval) 
wn.mainloop()