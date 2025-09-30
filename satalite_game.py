import time
import random
import pgzrun

HEIGHT=400
WIDTH=500

satalites=[]
pos_s=[]
previous_x=0
previous_y=0
n=0

while n<10:
    satalite=Actor("satalite")
    x=random.randint(25,475)
    y=random.randint(25,375)
    for i in pos_s:
        if x-i[0]<20 and y-i[1]<20:
          continue
    satalite.pos=x,y
    satalites.append(satalite)
    pos_s.append(satalite)
    n=n+1


def draw():
    screen.blit("galaxy",(0,0))
    for i in satalites:
        i.draw()



















pgzrun.go()
