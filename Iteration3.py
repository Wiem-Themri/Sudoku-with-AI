# Itération 2 : Partie graphique 

import numpy as np
import pygame
import time


grille = [              # Grille à résoudre
[2,0,0,0,0,0,0,4,0],
[0,0,0,0,0,0,5,0,0],
[0,1,0,6,0,4,0,3,8],
[1,0,0,7,4,0,0,8,9],
[0,0,9,0,8,0,1,0,0],
[0,0,0,0,9,5,0,0,4],
[8,9,0,4,0,7,0,1,0],
[0,0,2,0,0,0,0,0,0],
[0,3,0,0,0,0,0,0,7]]


def DrawGrid():
    # Draw the lines
    for i in range(9):
        for j in range(9):
            if grille[i][j] != 0:
                # couleur bleu pour les cases non vides
                pygame.draw.rect(screen, (137, 207, 240), (i * inc, j * inc, inc + 1, inc + 1))
                # insertion d'une valeur (de la matrice)
                text = a_font.render(str(grille[i][j]), True, (0, 0, 0))
                screen.blit(text, (i * inc + 22, j * inc + 19))
            else: # Si case vide, case blanche
                pygame.draw.rect(screen, (255, 255, 255), (i * inc, j * inc, inc + 1, inc + 1))
    # Dessin des bordures
    for i in range(10):
        if i % 3 == 0:
            width = 10  # chaque 3 cases -> ligne bold
        else:
            width = 5
        pygame.draw.line(screen, (228, 229, 231), (i * inc, 0), (i * inc, 500), width)  # verticale
        pygame.draw.line(screen, (228, 229, 231), (0, i * inc), (500, i * inc), width)  # horizontale


def DrawLoadingMessage():   # Message à afficher lors de la résolution du Sudoku
    text = a_font.render("Traitement En Cours...", True, (0, 0, 0))
    screen.blit(text, (150, 210))
    pygame.display.update()


def possible(x, y, n):      # Retourne True si le nombre n n'existe pas dans x, y 
    for i in range(0, 9):
        if grille[i][x] == n and i != y: # Vérifie si un nombre n existe dans une colonne x
            return False

    for i in range(0, 9):
        if grille[y][i] == n and i != x: # Vérifie si un nombre n existe dans une ligne y
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):  # Vérifie si le nombre n existe dans une région
            if grille[Y][X] == n:
                return False    
    return True

def resolution():          # Retourne la matrice résolue
    global grille
    for y in range(9):
        for x in range(9):
            if grille[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grille[y][x] = n
                        #time.sleep(1)
                        #DrawGrid()
                        #pygame.display.update()
                        #print("trying n = ", n , "at position y = ", y+1 , "and x = ", x+1)
                        #print(np.array(grille))
                        resolution()
                        grille[y][x] = 0
                        #time.sleep(1)
                        #DrawGrid()
                        #pygame.display.update()
                        #print("resetting to 0", "at position y = ", y+1 , "and x = ", x+1)
                        #print(np.array(grille))
                return
    DrawGrid()



# Main

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 500))  # Taille de la fenêtre
pygame.display.set_caption("Sudoku")  # Nom de la fenêtre
a_font = pygame.font.SysFont("Calibri", 20)  # Fonte
inc = 500 // 9 # Dimension d'une case
run = True
resolved = False
screen.fill((255, 255, 255))
DrawGrid() # Affichage de la grille initiale
pygame.display.update() # Mise à jour de l'écran pour afficher la grille
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
    if not(resolved):
        time.sleep(3)
        DrawLoadingMessage() # Afficher "Traitement en cours...."
        resolution()    # Résolution du Sudoku
        time.sleep(2)
        resolved = True
        pygame.display.update()