import time
from turtle import Screen
from jwe import Jwe
from machin import Machin
from score import Score

ekran = Screen()
ekran.setup(width=600, height=600)
ekran.tracer(0)

jwe = Jwe()

machine = Machin()

score = Score()

ekran.listen()
ekran.onkey(jwe.ale_anle, "Up")

lage = True
while lage:
    time.sleep(0.1)
    ekran.update()
    machine.krey()
    machine.avanse()

    for machin in machine.tout_machin:
        if machin.distance(jwe) < 20:
            lage = False
            score.fini()

    if jwe.rive():
        jwe.rekomanse()
        machine.ogmante()
        score.monte_nivo()

ekran.exitonclick()
