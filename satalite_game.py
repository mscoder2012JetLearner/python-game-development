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
c=0
n=10
ns=0

while c<10:
    satalite=Actor("satalite")
    x=random.randint(25,475)
    y=random.randint(25,375)

    satalite.pos=x,y
    satalites.append(satalite)
    pos_s.append(satalite)
    c=c+1


def draw():
    screen.blit("galaxy1",(0,0))
    r=1
    for i in satalites:
        i.draw()
        screen.draw.text(str(r),(i.pos[0],i.pos[1]+20),color="yellow")
        r=r+1
    #for i in pos_s:
        #print(i[0])
        #screen.draw.line(i[0],i[1],color="red")

    
def on_mouse_down(pos):
    global n,ns,pos_s
    if n>ns:
        if satalites[ns].collidepoint(pos):
            if ns==True:
                pos_s.append((satalites[ns-1].pos,satalites[ns].pos))
                print(pos_s)
            ns=ns+1
        else:
            pos_s=[]
            ns=0


 
    
    




pgzrun.go()