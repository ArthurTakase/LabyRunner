def goto_up(tab, x, y):
    if y - 2 < 0 :
        return "no"
    elif tab[y - 2][x] == "0":
        return "yes"
    else :
        return "no"

def goto_right(tab, x, y, xmax):
    if x + 2 >= xmax :
        return "no"
    elif tab[y][x + 2] == "0":
        return "yes"
    else :
        return "no"

def goto_down(tab, x, y, ymax):
    if y + 2 >= ymax :
        return "no"
    elif tab[y + 2][x] == "0":
        return "yes"
    else :
        return "no"

def goto_left(tab, x, y):
    if x - 2 < 0 :
        return "no"
    elif tab[y][x - 2] == "0":
        return "yes"
    else :
        return "no"
