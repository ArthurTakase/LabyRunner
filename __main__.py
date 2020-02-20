#--------------------------------------------
#
# Programme : LabyRunner
# Auteur    : Arthur DECAEN
# Date      : 04/02/2020
# Version   : Beta 1.2
#
#--------------------------------------------

import time
from random import *
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
    print("Pour une gestion dynamique de la taille de la fenetre du jeu, merci d'installer pyautogui sur votre machine.\npip install pyautogui")
    time.sleep(5)
    pygame.quit()
    quit()
from mainarcade import *

pygame.init()
pygame.display.set_caption('LabyRunner Beta 1.2')
icon = pygame.image.load("images/icon.png").convert_alpha()
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((max_width,max_height))

#font = pygame.font.SysFont(None, 20)

def button_click():
    button_1 = pygame.Rect(max_width//2-330, max_height//2+(max_height//6), 300, 125)
    button_2 = pygame.Rect(max_width//2+30, max_height//2+(max_height//6), 300, 125)

    back_image = pygame.image.load('images/background.png')
    back_image = pygame.transform.scale(back_image, (max_width, max_height))
    screen.blit(back_image, (0,0,max_width,max_height))

    button1 = pygame.image.load('images/arcade_button_up.png')
    button2 = pygame.image.load('images/libre_button_up.png')
    screen.blit(button2, button_2)
    screen.blit(button1, button_1)

    filtre = pygame.image.load('images/filtre_pixel.png')
    filtre = pygame.transform.scale(filtre, (max_width, max_height))
    screen.blit(filtre, (0,0,max_width,max_height))

    filtre2 = pygame.image.load('images/flou_bords.png')
    filtre2 = pygame.transform.scale(filtre2, (max_width, max_height))
    screen.blit(filtre2, (0,0,max_width,max_height))

    pygame.display.update()
    #time.sleep(0.2)

def main_menu():

    while True :
        #screen.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos() # [x,y]
        #mouse =

        button_1 = pygame.Rect(max_width//2-330, max_height//2+(max_height//6), 300, 125)
        button_2 = pygame.Rect(max_width//2+30, max_height//2+(max_height//6), 300, 125)
        if button_1.collidepoint((mx, my)) :
            if click :
                button_click()
                score = main_arcade()
                end_game(score)
        if button_2.collidepoint((mx, my)) :
            if click :
                button_click()
                tuto()
        button_click()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT :
                pygame.quit()
                quit()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    pygame.quit()
                    quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def end_button(score):
    button_1 = pygame.Rect(max_width//2-330, max_height//2+(max_height//6), 300, 125)
    button_2 = pygame.Rect(max_width//2+30, max_height//2+(max_height//6), 300, 125)

    back_image = pygame.image.load('images/game_over.png')
    back_image = pygame.transform.scale(back_image, (max_width, max_height))
    screen.blit(back_image, (0,0,max_width,max_height))

    button1 = pygame.image.load('images/restart_button_up.png')
    button2 = pygame.image.load('images/menu_button_up.png')
    screen.blit(button2, button_2)
    screen.blit(button1, button_1)

    text_draw(str(score), (max_width//2, max_height//2.6), (255,255,255), int((max_height-height)*1.25))

    filtre = pygame.image.load('images/filtre_pixel.png')
    filtre = pygame.transform.scale(filtre, (max_width, max_height))
    screen.blit(filtre, (0,0,max_width,max_height))

    filtre2 = pygame.image.load('images/flou_bords.png')
    filtre2 = pygame.transform.scale(filtre2, (max_width, max_height))
    screen.blit(filtre2, (0,0,max_width,max_height))

    pygame.display.update()


def end_game(score):
    '''Elements à montrer à la fin d'une run'''
    click = 0

    while True :
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(max_width//2-330, max_height//2+(max_height//6), 300, 125)
        button_2 = pygame.Rect(max_width//2+30, max_height//2+(max_height//6), 300, 125)

        if button_1.collidepoint((mx, my)) :
            if click :
                end_button(score)
                score = main_arcade()
                end_game(score)
        if button_2.collidepoint((mx, my)) :
            if click :
                end_button(score)
                return
        end_button(score)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT :
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def tuto():
    while True :
        back_image = pygame.image.load('images/tuto.png')
        back_image = pygame.transform.scale(back_image, (max_width, max_height))
        screen.blit(back_image, (0,0,max_width,max_height))

        filtre = pygame.image.load('images/filtre_pixel.png')
        filtre = pygame.transform.scale(filtre, (max_width, max_height))
        screen.blit(filtre, (0,0,max_width,max_height))

        filtre2 = pygame.image.load('images/flou_bords.png')
        filtre2 = pygame.transform.scale(filtre2, (max_width, max_height))
        screen.blit(filtre2, (0,0,max_width,max_height))

        for event in pygame.event.get():
            if event.type == QUIT :
                pygame.quit()
                quit()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    return

        pygame.display.update()

main_menu()
