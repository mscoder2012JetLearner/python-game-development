import time
import random
import pgzrun

HEIGHT=335
WIDTH=500
distance=100

bees=[]
pos_s=[]
previous_x=0
previous_y=0
n=0

while n<10:
    bee=Actor("bee")
    x=random.randint(25,475)
    y=random.randint(25,300)

    bee.pos=x,y
    bees.append(bee)
    pos_s.append(bee)
    n=n+1


def draw():
    screen.blit("bee background",(0,0))
    r=1
    for i in bees:
        i.draw()
        screen.draw.text(str(r),(i.pos[0],i.pos[1]+20),color="red")
        r=r+1


pgzrun.go()