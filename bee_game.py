import pgzrun
import random
import time#

HEIGHT=335
WIDTH=500

bee=Actor("bee")

def draw():
    screen.blit("bee background",(0,0))
    bee.draw()

pgzrun.go()

