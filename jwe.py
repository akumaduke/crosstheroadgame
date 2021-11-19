from turtle import Turtle


pozisyon_stat= (0, -280)
deplasman = 10
fini = 280


class Jwe(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.rekomanse()
        self.setheading(90)


    def ale_anle(self):
        self.fd(deplasman)



    def rekomanse(self):
        self.goto(pozisyon_stat)



    def rive(self):
        if self.ycor() >280:
            return True
        else:
            return False