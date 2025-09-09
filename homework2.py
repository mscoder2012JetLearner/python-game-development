import pgzrun
import random

HEIGHT=500
WIDTH=500
 

phoenix=Actor("phoenix")
messege="Hello"

def draw():
    screen.fill("blue")
    phoenix.draw()
    screen.draw.text(messege,center=(250,250),fontsize=(100))



pgzrun.go()

