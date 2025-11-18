import random
import pgzrun

HEIGHT=650
WIDTH=870

TITLE="quiz game"

answer_box1=Rect(0,0,300,150)
answer_box1.move_ip(20,270)

def draw():
    screen.draw.filled_rect(answer_box1,"red")










pgzrun.go()