import pgzrun
import random
import time

HEIGHT=500
WIDTH=500

alien=Actor("alien")
messege="hi alien"

def draw():
    screen.fill("gold")
    alien.draw()
    screen.draw.text(messege,center=(250,250),fontsize=(50))

def on_mouse_down(pos):
    global messege
    if alien.collidepoint(pos):
       messege="good shot"
       alien.x=random.randint(0,450)
       alien.y=random.randint(0,450)

    else:
        messege="you missed"
        



    







pgzrun.go()