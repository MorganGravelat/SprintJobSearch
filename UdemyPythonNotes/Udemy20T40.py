######################################################################MyTurtleCrossingWalkthrough
###This is my main as I have it setup now
from turtle import Screen #import Screen class from turtle module
from turtlep import TurtleP#This is my player class
from hud import HeadsUpDisplay#This is the HUD
import time #import time module

screen = Screen()#This is the screen
screen.bgcolor("white")#This is the background color
screen.setup(width=600, height=900)#This is the size of the screen
screen.title("Turtle Crossing")#This is the title of the screen
screen.tracer(0)#This turns the turtle animation off so I may update the screen at the pacing I want

player = TurtleP()#This is the player clone of the player class
player_hud = HeadsUpDisplay()#This is the HUD clone of the HUD class

screen.listen()#This is the screen listening for key presses
screen.onkey(player.go_up, "Up")#This is the screen listening for the up key press that moves the player up and through the course

game_is_on = True#This is the game on variable
while game_is_on:#This is the game on loop
    time.sleep(0.01)#This is the time delay for the screen update animation
    screen.update()#This is the screen update animation

screen.exitonclick()#This is the screen exit on click

##ITERATION2
from turtle import Screen
from turtlep import TurtleP
from hud import HeadsUpDisplay
from car import Car
import time
import random

screen = Screen()
screen.colormode(255)
screen.bgcolor("white")
screen.setup(width=600, height=900)
screen.title("Turtle Crossing")
screen.tracer(0)

player = TurtleP()
all_cars = []
for _ in range(30):
    test_car = Car()
    all_cars.append(test_car)

player_hud = HeadsUpDisplay()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    for car in all_cars:
        car.move()
        if (car.xcor() < -380):
            car.reset_position()
        screen.update()
    screen.update()


screen.exitonclick()
###LAST MAIN ITERATION
from turtle import Screen
from turtlep import TurtleP
from hud import HeadsUpDisplay
from car import Car
import time
import random

screen = Screen()
screen.colormode(255)
screen.bgcolor("white")
screen.setup(width=600, height=900)
screen.title("Turtle Crossing")
screen.tracer(0)
sleepy = 0.09
player = TurtleP()
all_cars = []
for _ in range(5):
    test_car = Car()
    all_cars.append(test_car)

player_hud = HeadsUpDisplay()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(sleepy)
    for car in all_cars:
        car.move()
        screen.update()
        if (car.xcor() < -380):
            car.reset_position()
        if car.distance(player) < 25:
            player_hud.game_over()
            screen.update()
            game_is_on = False
            break
    if player.ycor() > 380:
        player_hud.level_count+=1
        player_hud.update_level()
        player.reset_pos()
        sleepy *= 0.5
        for _ in range(5):
            test_car = Car()
            all_cars.append(test_car)
        print(sleepy)


    screen.update()


screen.exitonclick()

######################################################################MyTurtleCrossingMAINIterationsEND
###This is my current hud class.
from turtle import Turtle

class HeadsUpDisplay(Turtle): #This is the HUD class

    def __init__(self): #This is the HUD class init
        super().__init__() #This is the super that inherits from the Turtle class
        self.color("Black") #I setup the color and below I pull the pen up meaning I stop the turtle from drawing
        self.penup()
        self.hideturtle() #This is meant to draw a hud and that is why I hide the display of the body
        self.level_count = 1 #A variable to keep track of the level
        self.update_level() #This updates the level number and currently it is level 1

    def update_level(self):
        self.clear()##This clears the screen
        self.goto(-200, 380)#This is the location of the hidden turtle
        self.write(("Level: " + str(self.level_count)), align="center", font=("Courier", 25, "normal"))#This draws the first argument of self.write

    def game_over(self):
        self.goto(0, 0)#This is the location of the hidden turtle
        self.write("Game Over", align="center", font=("Courier", 50, "normal"))
###This is my current player class.
from turtle import Turtle


class TurtleP(Turtle):

    def __init__(self):
        super().__init__()##This is the same setup as the last but with different configurables
        self.shape("turtle")
        self.color("black")
        self.up()
        self.setheading(90)#This causes the player turtle to point up
        self.goto(0, -430)#This places the player turtle at the bottom of the screen

    def go_up(self):
        new_y = self.ycor() + 20#This is the new y coordinate that I set the player turtle to with the self.goto command
        self.goto(self.xcor(), new_y)
###This is my current car class
from turtle import Turtle
import random
import time
class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.r = random.randint(0, 255)  # Random red value
        self.g = random.randint(0, 255)  # Random green value
        self.b = random.randint(0, 255)  # Random blue value
        self.random_color = (self.r, self.g, self.b)
        self.color(self.random_color)#This is the color of the car
        self.startingpos = random.randint(-300, 400)#This is the starting position of the car
        self.startingxcor = random.randint(-300, 350)#This is the starting x coordinate
        self.shape("square")#This is the shape of the car
        self.penup()#This is the pen up
        self.goto(self.startingxcor, self.startingpos)  # This is the starting position of the car

    def move(self):
        time.sleep(random.randint(1, 9) / 100)
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def reset_position(self):
        self.startingpos = random.randint(-400, 400)
        self.goto(300, self.startingpos)
######################################################################MyTurtleCrossingFINAL CAR CLASS
from turtle import Turtle
import random
import time
class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.r = random.randint(0, 255)  # Random red value
        self.g = random.randint(0, 255)  # Random green value
        self.b = random.randint(0, 255)  # Random blue value
        self.random_color = (self.r, self.g, self.b)
        self.color(self.random_color)
        self.startingpos = random.randint(-350, 400)
        self.startingxcor = random.randint(-300, 350)
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.goto(self.startingxcor, self.startingpos)

    def move(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def reset_position(self):
        self.startingpos = random.randint(-390, 400)
        self.goto(300, self.startingpos)

######################################################################MyTurtleCrossingFINAL PLAYER CLASS
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)






window.mainloop()
######Timer Mechanism
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
######Reset Timer
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
######Countdown Mechanism
from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
