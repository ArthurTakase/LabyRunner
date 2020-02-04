from random import choice, randint
from goto import *

def move(tab, y, x, ymax, xmax):
    move_ok = False

    while not move_ok :
        choix = randint(0,3)
        if choix == 0 :
            # Aller en haut
            if goto_up(tab, x, y) == "yes" :
                move_ok = True
                #print("up")
                y -= 2
                tab[y][x] = "1"
                tab[y+1][x] = "1"
        elif choix == 1 :
            # Aller à droite
            if goto_right(tab, x, y, xmax) == "yes" :
                #print("right")
                move_ok = True
                x += 2
                tab[y][x] = "1"
                tab[y][x-1] = "1"
        elif choix == 2 :
            # Aller en bas
            if goto_down(tab, x, y, ymax) == "yes" :
                #print("down")
                move_ok = True
                y += 2
                tab[y][x] = "1"
                tab[y-1][x] = "1"
        else :
            # Aller à gauche
            if goto_left(tab, x, y) == "yes" :
                #print("left")
                move_ok = True
                x -= 2
                tab[y][x] = "1"
                tab[y][x+1] = "1"

    return y,x
