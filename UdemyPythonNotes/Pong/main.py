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
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)


screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

game_on = True

while game_on:
    screen.update()

screen.exitonclick()
