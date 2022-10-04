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
