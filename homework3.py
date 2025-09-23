import pgzrun
import random
import time

HEIGHT=375
WIDTH=500

game_over=False
score=0

jerry=Actor("jerry")
jerry.pos=250,250
tom=Actor("tom")

def draw():
    screen.blit("t j bg",(0,0))
    jerry.draw()
    tom.draw()
    screen.draw.text("score= "+str(score),color="white",topleft=(10,10))
    if game_over==True:
        screen.fill("black")
        screen.draw.text("score= "+str(score),color="white",topleft=(10,10))
        screen.draw.text("GAME OVER!",color="white",topleft=(225,175))



def update():
    global score
    if keyboard.left:
        tom.x=tom.x-5
    if keyboard.right:
        tom.x=tom.x+5
    if keyboard.up:
        tom.y=tom.y-5
    if keyboard.down:
        tom.y=tom.y+5
    if tom.colliderect(jerry):
        x=random.randint(10,490)
        y=random.randint(10,330)
        jerry.x=x
        jerry.y=y
        score=score+1
        
def end():
    global game_over
    game_over=True
clock.schedule(end,30)


pgzrun.go()

