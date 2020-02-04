def end(tab, ymax, xmax):
    count = 0
    for y in range (len(tab)) :
        for x in range(len(tab[y])) :
            if tab[y][x] == "0" :
                count += 1

    if count == 1 and tab[ymax-1][xmax-1] == "0" :
        tab[ymax-1][xmax-1] = "1" # Fin du laby
        tab[ymax-2][xmax-1] = "1" # Modif ici
        return True
    if count != 0 :
        return False
    else :
        return True
