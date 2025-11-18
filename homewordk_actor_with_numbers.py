import time
import random
import pgzrun

HEIGHT=300
WIDTH=500
distance=100

bees=[]
pos_s=[]
previous_x=0
previous_y=0
c=0
n=10
ns=0

while c<10:
    bee=Actor("bee")
    x=random.randint(25,475)
    y=random.randint(25,275)

    bee.pos=x,y
    bees.append(bee)
    c=c+1


def draw():
    screen.blit("bee background",(0,0))
    r=1
    for i in bees:
        i.draw()
        screen.draw.text(str(r),(i.pos[0],i.pos[1]+20),color="blue")
        r=r+1
    for i in pos_s:
        print(i[0])
        screen.draw.line(i[0],i[1],color="red")

    
def on_mouse_down(pos):
    global n,ns,pos_s
    if n>ns:
        if bees[ns].collidepoint(pos):
            if ns:
                pos_s.append((bees[ns-1].pos,bees[ns].pos))
                print(pos_s)
            ns=ns+1
            print(ns)
        else:
            pos_s=[]
            ns=0


 
    
    




pgzrun.go()