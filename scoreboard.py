from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self, ):
        self.score = 0
        super().__init__()
        self.write.("Score:" + str(self.score), move = False, align = "center" ,font = ("Arial", 8, "normal") )
