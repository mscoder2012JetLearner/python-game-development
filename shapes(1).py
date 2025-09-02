import pgzrun
import random

WIDTH=500
HEIGHT=500

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)



def draw():
    w=500
    h=500
    for i in range(100):
      rect=Rect((0,0),(w,h))
      rect.center=250,250
      screen.draw.rect(rect,(r,g,b))
      w=w-10
      h=h-10


pgzrun.go()