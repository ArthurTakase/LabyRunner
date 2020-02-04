def print_laby(tab): # Print le labyrinthe
    tab_str = ""

    for i in range (len(tab)) :
        for j in range (len(tab[i])) :
            if i == 0 and j == 0 :
                tab_str += "DD"
            elif i == len(tab)-1 and j == len(tab[i])-1:
                tab_str += "FF"
            elif tab[i][j] == "0" :
                tab_str += "00"
            elif tab[i][j] == "1" :
                tab_str += "  "
            else :
                tab_str += "XX"
                #tab_str += tab[i][j]
        tab_str += "\n"

    print(tab_str)
