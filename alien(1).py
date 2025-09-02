import pgzrun
import random

HEIGHT=500
WIDTH=500

alien=Actor("alien")
messege="hi alien"

def draw():
    screen.fill("gold")
    alien.draw()
    screen.draw.text(messege,center=(250,250),fontsize=(100))




pgzrun.go()