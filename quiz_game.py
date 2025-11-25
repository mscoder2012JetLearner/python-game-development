import random
import pgzrun

HEIGHT=650
WIDTH=870

TITLE="quiz game"

answer_box1=Rect(0,0,300,150)
answer_box1.move_ip(20,270)

answer_box2=Rect(0,0,300,150)
answer_box2.move_ip(350,270)

answer_box3=Rect(0,0,300,150)
answer_box3.move_ip(20,450)

answer_box4=Rect(0,0,300,150)
answer_box4.move_ip(350,450)

def draw():
    screen.draw.filled_rect(answer_box1,"red")
    screen.draw.filled_rect(answer_box2,"red")
    screen.draw.filled_rect(answer_box3,"red")
    screen.draw.filled_rect(answer_box4,"red")
   












pgzrun.go()