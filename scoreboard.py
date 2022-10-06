from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.color("white")
        self.hideturtle()
        self.score1=0
        self.score2=0
        self.update_score()

    def update_score(self):
        self.pu()
        self.clear()
        self.goto(-40,self.height/2-60)
        self.pd()
        self.write(f"{self.score1}",align=ALIGNMENT,font=FONT)
        self.pu()
        self.goto(40, self.height / 2 - 60)
        self.pd()
        self.write(f"{self.score2}", align=ALIGNMENT, font=FONT)


    def increase_score1(self):
        self.score1+=1
        self.update_score()

    def increase_score2(self):
        self.score2+=1
        self.update_score()
        
    def final(self, won):
        if(won == 1):
            self.score1 = "Won"
            self.score2 = "Lost"
        else:
        	self.score1 = "Lost"
        	self.score2 = "Won"
        self.pu()
        self.clear()
        self.goto(-60,self.height/2-60)
        self.pd()
        self.write(f"{self.score1}",align=ALIGNMENT,font=FONT)
        self.pu()
        self.goto(60, self.height / 2 - 60)
        self.pd()
        self.write(f"{self.score2}", align=ALIGNMENT, font=FONT)
