import pgzrun
import random

WIDTH=500
HEIGHT=500

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

def draw():
    rect=Rect((50,50),(200,200))
    screen.draw.rect(rect,(r,g,b))

pgzrun.go()