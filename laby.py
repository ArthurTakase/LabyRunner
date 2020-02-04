from move import *
from printlaby import *
from newway import *
from goto import *
from end import *
import time

def gen(xmax, ymax) : # genere le tableau de base
    tab = []
    for y in range(ymax):
        line = []
        for x in range(xmax):
            if y == 0 and x == 0 :
                line.append("1")
            elif y == ymax - 1 and x == xmax - 1 :
                line.append("0")
            else :
                if y % 2 == 0 :
                    if x % 2 != 0 :
                        line.append("X")
                    else :
                        line.append("0")
                else :
                     line.append("X")
        tab.append(line)

    y = 0
    x = 0
    while not end(tab, ymax, xmax) :
        y, x = move(tab, y, x, ymax, xmax)
        if goto_up(tab, x, y) == "no" and goto_down(tab, x, y, ymax) == "no" and goto_left(tab, x, y) == "no" and goto_right(tab, x, y, xmax) == "no" and not end(tab, ymax, xmax):
                x, y = newway(tab, ymax, xmax)

    return tab
