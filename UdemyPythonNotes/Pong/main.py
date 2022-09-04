# paddle
# ball
#enempy paddle which inherits from paddle
#Create the screen
#Create and move a paddle
#Create another paddle
#create the ball and make it move
#detect collision with wall and bounce
# Detect collision with paddle
#Detect when paddle misses
#Keep score
from turtle import Screen, Turtle
from paddly import Paddle
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
#screen.tracer(0)

paddle = Paddle()


screen.listen()
screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")

screen.exitonclick()
