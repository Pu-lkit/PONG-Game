from turtle import Turtle
from random import choice
BALL_STEPS=2


class Ball(Turtle):

    def __init__(self,height,width):
        super().__init__(shape="circle")
        self.color("white")
        self.setheading(225)
        self.ihead=225
        self.height=height
        self.width=width
        self.pu()

    def move(self):
        self.forward(BALL_STEPS)
        if self.ycor()>=self.height/2-30 or self.ycor()<=-self.height/2+30:
            self.setheading(360-self.heading())

    def out(self):
        self.home()
        self.ihead+=90
        self.setheading(self.ihead%360)

    def collide(self):
        self.setheading(540-self.heading())
