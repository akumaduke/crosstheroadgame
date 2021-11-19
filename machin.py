from turtle import Turtle
import random

koule = ["red", "orange", "yellow", "green", "blue", "purple"]
mouvman = 5
mouvman_nivo = 10


class Machin:
    def __init__(self):
        self.tout_machin = []
        self.vites= mouvman

    def krey(self):
        chans=random.randint(1,6)
        if chans ==1:
            nouvo_machin=Turtle("square")
            nouvo_machin.shapesize(stretch_wid=1, stretch_len=2)
            nouvo_machin.penup()
            nouvo_machin.color(random.choice(koule))
            y_kelkonk= random.randint(-250, 250)
            nouvo_machin.goto(300,y_kelkonk)
            self.tout_machin.append(nouvo_machin)


    def avanse(self):
        for machin in self.tout_machin:
            machin.backward(self.vites)


    def ogmante(self):
        self.vites += mouvman_nivo