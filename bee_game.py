import pgzrun
import random
import time

HEIGHT=335
WIDTH=500

game_over=False
score=0

bee=Actor("bee")
bee.pos=250,250
eagle=Actor("eagle")

def draw():
    screen.blit("bee background",(0,0))
    bee.draw()
    eagle.draw()
    screen.draw.text("score= "+str(score),color="white",topleft=(10,10))
    if game_over==True:
        screen.fill("black")
        screen.draw.text("score= "+str(score),color="white",topleft=(10,10))
        screen.draw.text("GAME OVER!",color="white",topleft=(250,250))



def update():
    global score
    if keyboard.left:
        eagle.x=eagle.x-5
    if keyboard.right:
        eagle.x=eagle.x+5
    if keyboard.up:
        eagle.y=eagle.y-5
    if keyboard.down:
        eagle.y=eagle.y+5
    if eagle.colliderect(bee):
        x=random.randint(10,490)
        y=random.randint(10,330)
        bee.x=x
        bee.y=y
        score=score+1
        
def end():
    global game_over
    game_over=True
clock.schedule(end,60)


pgzrun.go()

