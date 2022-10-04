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
