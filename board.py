from turtle import Turtle


class Board:

    def __init__(self, position,height):
        self.squares = []
        self.positions = position
        self.make_board()
        self.height=height
        self.board_limit_up=position[0][1]+10
        self.board_limit_down=position[-1][1]-10

    def make_board(self):
        for i in range(5):
            tim = Turtle("square")
            tim.pu()
            tim.color("white")
            x_cor = self.positions[i][0]
            y_cor = self.positions[i][1]
            tim.goto(x_cor, y_cor)
            self.squares.append(tim)

    def up(self):
        if self.squares[0].ycor() <= self.height/2-30:
            for item in self.squares:
                item.setheading(90)
                item.forward(20)
            self.board_limit_up+=20
            self.board_limit_down+=20

    def down(self):
        if self.squares[-1].ycor() >= -self.height / 2 +30:
            for item in self.squares:
                item.setheading(270)
                item.forward(20)
            self.board_limit_up-=20
            self.board_limit_down-=20
