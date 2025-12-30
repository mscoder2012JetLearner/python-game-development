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
    screen.draw.filled_rect(answer_box1,"white")
    screen.draw.filled_rect(answer_box2,"white")
    screen.draw.filled_rect(answer_box3,"white")
    screen.draw.filled_rect(answer_box4,"white")
    screen.draw.filled_rect(question_box,"red")
    screen.draw.filled_rect(timer_box,"green")
    screen.draw.filled_rect(skip_box,"blue")
    screen.draw.filled_rect(intro_box,"orange")
    screen.draw.textbox("Welcome to Quizz master!",intro_box,color="white")
    screen.draw.textbox("Skip",skip_box,color="black",angle=90,shadow=(0.5,0.5),scolor="light gray")
    screen.draw.textbox(str(time),timer_box,color="black",shadow=(0.5,0.5),scolor="light gray")
    screen.draw.textbox(Q[0],question_box,color="black",shadow=(0.5,0.5),scolor="light gray")
    screen.draw.textbox(Q[1],answer_box1,color="black",shadow=(0.5,0.5),scolor="light gray")
    screen.draw.textbox(Q[2],answer_box2,color="black",shadow=(0.5,0.5),scolor="light gray")
    screen.draw.textbox(Q[3],answer_box3,color="black",shadow=(0.5,0.5),scolor="light gray")
    screen.draw.textbox(Q[4],answer_box4,color="black",shadow=(0.5,0.5),scolor="light gray")

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

file_storage="C:/Users/31mschwarz/OneDrive - Abbey Gate College/Documents and subjects/python game developer/questions.txt"
list_of_questions=[]

def question_reader():
    global list_of_questions
    open_file=open(file_storage,"r")
    for i in open_file:
        list_of_questions.append(i)
    open_file.close()
def read_question():
    random.shuffle(list_of_questions)
    return list_of_questions.pop(0).split(",")
question_reader()
Q=read_question()
print(Q)
def on_mouse_down(pos):
    pass


    
pgzrun.go()