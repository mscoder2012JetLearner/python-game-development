import random
import pgzrun
import os
os.environ['SDL_VIDEO_CENTERED']='1'

time=10
HEIGHT=670
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

question_box=Rect(0,0,630,100)
question_box.move_ip(20,150)

timer_box=Rect(0,0,100,100)
timer_box.move_ip(675,150)

skip_box=Rect(0,0,150,330)
skip_box.move_ip(675,270)

intro_box=Rect(0,0,755,100)
intro_box.move_ip(20,20)



def draw():
    screen.fill(color="black")
    screen.draw.filled_rect(answer_box1,"red")
    screen.draw.filled_rect(answer_box2,"red")
    screen.draw.filled_rect(answer_box3,"red")
    screen.draw.filled_rect(answer_box4,"red")
    screen.draw.filled_rect(question_box,"magenta")
    screen.draw.filled_rect(timer_box,"blue")
    screen.draw.filled_rect(skip_box,"dark green")
    screen.draw.filled_rect(intro_box,"mediumvioletred")
    screen.draw.textbox("Welcome to Quizz master!",intro_box,color="white")
    screen.draw.textbox("Skip",skip_box,color="white",angle=90,shadow=(0.5,0.5))
    screen.draw.textbox(str(time),timer_box,color="white",shadow=(0.5,0.5))

def update():
    intro_box.x-=2
    if intro_box.right<0:
        intro_box.left=870
def time_update():
    global time 
    time=time-1
    if time<=0:
        time=0
clock.schedule_interval(time_update,1)






   












pgzrun.go()