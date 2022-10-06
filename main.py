import turtle as t
from board import Board
from scoreboard import Scoreboard
from ball import Ball
from time import sleep

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BOARD_LINE = 30
SLEEP_TIME=0.006
POSITIONS1 = [(BOARD_LINE-SCREEN_WIDTH/2, 40),
              (BOARD_LINE-SCREEN_WIDTH/2, 20),
              (BOARD_LINE-SCREEN_WIDTH/2, 0),
              (BOARD_LINE-SCREEN_WIDTH/2, -20),
              (BOARD_LINE-SCREEN_WIDTH/2, -40)
              ]
POSITIONS2 = [(SCREEN_WIDTH/2-BOARD_LINE, 40),
              (SCREEN_WIDTH/2-BOARD_LINE, 20),
              (SCREEN_WIDTH/2-BOARD_LINE, 0),
              (SCREEN_WIDTH/2-BOARD_LINE, -20),
              (SCREEN_WIDTH/2-BOARD_LINE, -40)
              ]

screen = t.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

scoreboard=Scoreboard(SCREEN_WIDTH,SCREEN_HEIGHT)

board1=Board(POSITIONS1,SCREEN_HEIGHT)
board2=Board(POSITIONS2,SCREEN_HEIGHT)

line = t.Turtle()
line.hideturtle()
line.color("white")
ball=Ball(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)

def make_center_line():
    line.pu()
    line.goto(0, -SCREEN_HEIGHT / 2)
    line.pd()
    line.setheading(90)
    while line.ycor() < SCREEN_HEIGHT / 2 + 20:
        line.pd()
        line.forward(10)
        line.pu()
        line.forward(10)


make_center_line()
screen.update()

screen.listen()
screen.onkey(board2.up, "Up")
screen.onkey(board2.down, "Down")
screen.onkey(board1.up, "w")
screen.onkey(board1.down, "s")


def check_collision():
    if ball.xcor() < -SCREEN_WIDTH / 2 + 40:
        if board1.board_limit_up+10 >= ball.ycor() >= board1.board_limit_down-10:
            ball.collide()
        else:
            ball.out()
            scoreboard.increase_score2()

    if ball.xcor() > SCREEN_WIDTH / 2 - 45:
        if board2.board_limit_up+10 >= ball.ycor() >= board2.board_limit_down-10:
            ball.collide()
        else:
            ball.out()
            scoreboard.increase_score1()


is_game_on=True
player1 = True
winning_score = 5
while(is_game_on):
    ball.move()
    check_collision()
    sleep(SLEEP_TIME)
    screen.update()
    if scoreboard.score1==winning_score:
        is_game_on=False
        player1=True
        
    if scoreboard.score2==winning_score:
        is_game_on=False
        player1=False
        
        
if(player1):
    scoreboard.final(1)
else:
	scoreboard.final(2)
screen.exitonclick()
