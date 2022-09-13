from turtle import Turtle

class Paddle:
    def __init__(self,posX, posY):
        self.paddle = Turtle()
        self.paddle.up()
        self.paddle.goto(posX, posY)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        (posX, posY) = self.paddle.pos()
        self.paddle.setpos(posX, (posY+20))

    def down(self):
        (posX, posY) = self.paddle.pos()
        self.paddle.setpos(posX, (posY-20))
