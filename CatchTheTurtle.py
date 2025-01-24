import turtle as t
import time
import threading
import random

wn_ins = t.Screen()
wn_ins.bgcolor("lightblue")
wn_ins.title("Catch The Turtle")



scoreBoard = t.Turtle()
scoreBoard.hideturtle()
scoreBoard.penup()
scoreBoard.color("blue")
scoreBoard.goto(0, 350)
scoreBoard.write("Score: 0 ", align="center", font=("Arial", 24, "bold"))

timer_text = t.Turtle()
timer_text.hideturtle()
timer_text.penup()
timer_text.color("black")
timer_text.goto(0, 300)

button=t.Turtle()


sayac = 15
score = 0

def handleScore():
    global score
    score += 1
    wn_ins.update()
    scoreBoard.goto(0,350)
    scoreBoard.clear()
    scoreBoard.write(f"Score :  {score}" , align="center", font=("Arial", 24, "bold"))


def handleButtonClick(x,y):
    x=0
    y=0
    wn_ins.update()
    button.clear()
    handleScore()


def randomTurtle():
    button.penup()
    button.color("green")
    button.shape("turtle")
    button.shapesize(stretch_wid=2, stretch_len=2)
    _x = random.randint(-280,280)
    _y = random.randint(-280,280)
    button.setpos(_x,_y)
    if sayac != 0:
        time.sleep(0.300)
        randomTurtle()
    elif sayac == 0:
        button.hideturtle()


def timerTextHandler():
    global sayac
    timer_text.clear()
    timer_text.write(f"Time:{sayac} ", align="center", font=("Arial", 24, "bold"))
    time.sleep(1)
    sayac -=1
    wn_ins.update()
    if sayac != 0:
        timerTextHandler()
    elif sayac == 0:
        timer_text.clear()
        timer_text.write(f"Süren Bitti.. ", align="center", font=("Arial", 24, "bold"))

Timer = threading.Thread(target=timerTextHandler , daemon=True)
Timer.start()
randomT = threading.Thread(target=randomTurtle, daemon=True)
randomT.start()


button.onclick(fun=handleButtonClick)
t.listen()
t.mainloop()