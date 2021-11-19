from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.nivo=1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.ekri()


    def ekri(self):
        self.clear()
        self.write(f"nivo{self.nivo}", align="Left", font=FONT)


    def monte_nivo(self):
        self.nivo+=1
        self.ekri()


    def fini(self):
        self.goto(0,0)
        self.write(f"OU PEDI", align="center", font=FONT)