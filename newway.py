from random import randint
from goto import *

def newway(tab, ymax, xmax):
    x, y = 1, 1
    while x % 2 != 0 or y % 2 != 0 :
        if x % 2 != 0 :
            x = randint(0, xmax - 1)
        if y % 2 != 0 :
            y = randint(0, ymax - 1)

    while (goto_up(tab, x, y) == "no" and goto_down(tab, x, y, ymax) == "no" and goto_left(tab, x, y) == "no" and goto_right(tab, x, y, xmax) == "no") or tab[y][x] != "1" :
        x += 2
        if x >= xmax :
            y += 1
            x = 0
        if y >= ymax :
            y = 0

    return x,y
