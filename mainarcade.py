# ---- Import ----
import time
from laby import *
from random import randint
import random
try :
    import pygame
    from pygame.locals import *
except :
    print("Pour pouvoir utiliser ce programme, merci d'installer Pygame sur votre machine.\npip install pygame")
    time.sleep(5)
    exit()
try : # Ajustement automatique de la fenetre du programme
    import pyautogui
    screen_size = pyautogui.size()
    max_width = int(screen_size[1] / 1.1)
    max_height = max_width
    width = int(screen_size[1] / 1.13)
    height = width
except : # Valeur de la fenetre par défaut
    print("Pour une gestion dynamique de la taille le la fenetre du jeu, merci d'installer pyautogui sur votre machine.\npip install pyautogui")
    time.sleep(5)
    exit()


# ---- Init ----
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((max_width,max_height))
pygame.display.set_caption('LabyRunner Beta 1.2') # Nom de la fenetre
pygame.mixer.music.load("sons/back_music.mp3")
pygame.mixer.music.set_volume(0.02)
pygame.mixer.music.play(-1)
score = 0
bonus = 0


# ---- Color ----
BLACK = (41, 40, 66)
WHITE = (82, 105, 115)
RED = (239, 231, 181)
BLUE = (165, 170, 198)
YELLOW = (224, 219, 138)
CYAN = (122, 206, 201)


# ---- Variables des Dessins ----
xmax = 5 # Valeur du plus petit laby
ymax = xmax
lenthx = int(width / xmax)
lenthy = int(height / ymax)


# ---- Set Timer ----
end = 0
last_end = -1
bonus = 0
countdown = 90


# ---- Surfaces ----
screen.fill(BLACK)
pygame.display.update()
labyrinthe = pygame.Surface((width, height))
image = pygame.Surface((int(lenthx/1.5), int(lenthy/1.5)))
rect = image.get_rect()
rect[0], rect[1] = int(lenthx/6), int(lenthy/6)
image.fill(RED)


# ---- Génération GRAPHIQUE du labyrinthe ----
def gen_laby(xmax, ymax) :
    '''Transforme le labyrinthe créé par laby.py en forme graphique.
    Les dimensions sont données en arguments.
    Des bonus apparraissent de manière aléatoire dans les cases blanches.'''

    lenthx = int(width / xmax)
    lenthy = int(height / ymax)

    tab = gen(xmax,ymax)
    pygame.draw.rect(labyrinthe, BLACK, (0,0,max_width,max_height))

    for y in range (ymax):
        for x in range(xmax):
            centrex = int(x*lenthx+lenthx/2)
            centrey = int(y*lenthy+lenthy/2)

            if y == ymax - 1 and x == xmax - 1 :
                pygame.draw.rect(labyrinthe, BLUE, (x*lenthx,y*lenthy,lenthx+1,lenthy+1))

            elif tab[y][x] == "X" :
                pygame.draw.rect(labyrinthe, BLACK, (x*lenthx,y*lenthy,lenthx+1,lenthy+1))

            else :
                if random.randint(0,75) == 0 : # Génération des bonus
                    pygame.draw.rect(labyrinthe, WHITE, (x*lenthx,y*lenthy,lenthy+1,lenthx+1))
                    pygame.draw.circle(labyrinthe, YELLOW, (centrex,centrey), int(lenthy/4))

                elif random.randint(0,80) == 0 : # Génération des bonus
                    pygame.draw.rect(labyrinthe, WHITE, (x*lenthx,y*lenthy,lenthy+1,lenthx+1))
                    pygame.draw.circle(labyrinthe, CYAN, (centrex,centrey), int(lenthy/4))

                else :
                    pygame.draw.rect(labyrinthe, WHITE, (x*lenthx,y*lenthy,lenthy+1,lenthx+1))


# ---- Afficher texte ----
def text_draw(text, position, color, size):
    '''affiche le texte demandé dans la couleur et la position choisie.'''

    myfont = pygame.font.SysFont('Comic Sans MS', size)
    textsurface = myfont.render(text, True, color)
    screen.blit(textsurface,position)


# ---- Effacement bonus ----
def set_color(color,numero) :
    '''Change la couleur de la case où se trouve le joueur si appelée.
    La couleur est donné en argument (tuple, voir la liste des couleurs au début du programme)'''

    pygame.draw.rect(labyrinthe, color, (int(rect[0]-(lenthx/6)+1),int(rect[1]-(lenthx/6)+1),lenthy-1,lenthx-1)) # On recouvre les bonus par dublanc
    affiche(numero)


# ---- Mouvement carré rouge ----
def move(x,y,numero):
    '''Deplace le joueur en fonction des valeurs données en arguments en gardant la labyrinthe en fond.'''

    rect.move_ip(int(x), int(y))
    affiche(numero)


# ---- Met à jour l'affichage des différents éléments ----
def affiche(numero):
    '''Met à jour l'affichage des différents éléments que doit voir le joueur'''
    global score, end, countdown

    screen.fill(BLACK)
    screen.blit(labyrinthe, (0,0))
    screen.blit(image, rect)

    final_str = "Score : " + str(score) + " // Temps : " + str(countdown - end)
    text_draw(final_str, (0, int(max_height - (max_height-height))), (255,255,255), int((max_height-height)/2))

    filtre = pygame.image.load('images/bruit_'+ str(numero) +'.png')
    #filtre = pygame.image.load('images/filtre_pixel.png')
    filtre = pygame.transform.scale(filtre, (max_width, max_height))
    screen.blit(filtre, (0,0,max_width,max_height))

    filtre2 = pygame.image.load('images/flou_bords.png')
    filtre2 = pygame.transform.scale(filtre2, (max_width, max_height))
    screen.blit(filtre2, (0,0,max_width,max_height))

    pygame.display.update()

# ---- Input utilisateur ----
# continu
def run(mode,numero):
    '''Deplacement du personne '''

    if mode == "rapide" :
        vitesse = 0.03
        if pressedKeys[K_UP] and rect[1] - lenthy > 0 :
            if labyrinthe.get_at((rect[0], rect[1] - int(lenthy))) != BLACK :
                move(0, -lenthy,numero)
                time.sleep(vitesse)
        if pressedKeys[K_DOWN]  and rect[1] + lenthy < height:
            if labyrinthe.get_at((rect[0], rect[1] + int(lenthy))) != BLACK :
                move(0, lenthy,numero)
                time.sleep(vitesse)
        if pressedKeys[K_LEFT] and rect[0] - lenthx > 0:
            if labyrinthe.get_at((rect[0] - int(lenthx), rect[1])) != BLACK :
                move(-lenthy,0,numero)
                time.sleep(vitesse)
        if pressedKeys[K_RIGHT] and rect[0] + lenthx < width :
            if labyrinthe.get_at((rect[0] + int(lenthx), rect[1])) != BLACK :
                move(lenthy,0,numero)
                time.sleep(vitesse)

    elif mode == "lent" :
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP and rect[1] - lenthy > 0:
                    if labyrinthe.get_at((rect[0], rect[1] - int(lenthy))) != BLACK :
                        move(0, -lenthy,numero)

                if event.key == pygame.K_DOWN and rect[1] + lenthy < height:
                    if labyrinthe.get_at((rect[0], rect[1] + int(lenthy))) != BLACK :
                        move(0, lenthy,numero)

                if event.key == pygame.K_LEFT and rect[0] - lenthx > 0:
                    if labyrinthe.get_at((rect[0] - int(lenthx), rect[1])) != BLACK :
                            move(-lenthy,0,numero)

                if event.key == pygame.K_RIGHT and rect[0] + lenthx < width:
                    if labyrinthe.get_at((rect[0] + int(lenthx), rect[1])) != BLACK :
                        move(lenthy,0,numero)

def fin():
    '''Elements à montrer à la fin d'une run'''

    screen.fill(BLACK)
    text_draw("FINI !", ((max_width/2.1)-100, (max_height/2.1)-100), (255,255,255), 100)
    final_score = "Score : " + str(score) + " points"
    final_time ="Temps joué : " + str(end+bonus) + " secondes"
    text_draw(final_score, (10, max_height - (max_height-height)*2-2*xmax), (255,255,255), int(max_height-height))
    text_draw(final_time, (10, max_height - (max_height-height)-2*xmax), (255,255,255), int(max_height-height))
    pygame.display.update()


# ---- Boucle de jeu ----
def main_arcade():
    global xmax, ymax, end, bonus, last_end, pressedKeys,lenthx, lenthy, image, score
    numero = random.randint(1,2)
    # à initialiser à chaque partie
    end = 0
    xmax = 5 # Valeur du plus petit laby
    ymax = xmax
    lenthx = int(width / xmax)
    lenthy = int(height / ymax)
    image = pygame.transform.scale(image, (int(lenthx/1.5),int(lenthy/1.5)))

    rect[0], rect[1] = int(lenthx/6), int(lenthy/6)
    pygame.display.update()
    score = 0
    bonus = 0

    # Chargement
    loading = pygame.image.load('images/loading.png')
    loading = pygame.transform.scale(loading, (max_width, max_height))
    screen.blit(loading, (0,0,max_width,max_height))
    pygame.display.update()

    # Premier affichage
    gen_laby(xmax, ymax)
    start = time.time()
    affiche(numero)

    # Interactions
    while end != countdown: # Le jeu se stop au bout de x secondes
        affiche(numero)
        end = int(time.time() - start - bonus)
        if end != last_end :
            last_end = end
            affiche(numero)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()

        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[K_SPACE] :
            # Deplacement case par case, appui par appui
            run("lent",numero)
        else :
            # Deplacement rapide
            run("rapide",numero)

        # ---- Bonus ----
        # Bonus Bleu : +25 points
        if labyrinthe.get_at((int(rect[0]+(lenthx/3.5)), int(rect[1]+(lenthy/3.5)))) == CYAN :
            score += 25
            set_color(WHITE,numero)

        # Bonus Jaune : +5 secondes
        if labyrinthe.get_at((int(rect[0]+(lenthx/3.5)), int(rect[1]+(lenthy/3.5)))) == YELLOW :
            bonus += 5
            set_color(WHITE,numero)

        # ---- Victoire ----
        if labyrinthe.get_at((rect[0], rect[1])) == BLUE :
            # Generation d'une nouveau laby plus grand
            xmax += 2
            ymax += 2
            gen_laby(xmax, ymax)

            # modification du joueur
            lenthx = int(width / xmax)
            lenthy = int(height / ymax)
            rect[0], rect[1] = int(lenthx/6), int(lenthy/6) # Set le joueur au debut du labby
            image = pygame.transform.scale(image, (int(lenthx/1.5),int(lenthy/1.5))) # Set la taille du joueur par raport à celle des murs
            rect[2], rect[3] = int(lenthx/1.5),int(lenthy/1.5) # Set la hitbox du joueur

            # Update
            score += 100
            bonus += 5
            numero = random.randint(1,2)
            affiche(numero)

    return score
