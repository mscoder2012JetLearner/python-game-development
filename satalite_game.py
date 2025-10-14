import time
import random
import pgzrun

HEIGHT=400
WIDTH=500
distance=100

satalites=[]
pos_s=[]
previous_x=0
previous_y=0
n=0

while n<10:
    satalite=Actor("satalite")
    x=random.randint(25,475)
    y=random.randint(25,375)

    satalite.pos=x,y
    satalites.append(satalite)
    pos_s.append(satalite)
    n=n+1


def draw():
    screen.blit("galaxy1",(0,0))
    r=1
    for i in satalites:
        i.draw()
        screen.draw.text(str(r),(i.pos[0],i.pos[1]+20))
        r=r+1


pgzrun.go()
