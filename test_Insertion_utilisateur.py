import time
import numpy as np

grille = [ ]

while True :
    row = list(input('Insérer une ligne de la grille : '))
    Liste = []

    for i in row :
        Liste.append(int(i))
    grille.append(Liste)

    if len(grille) == 9 :
        print('Grille complète')
        break
        
time.sleep(1)

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
                        resolution()
                        grille[y][x] = 0
                return
    print('\n', np.array(grille))
    input('\n Sudoku résolu !\n') # A corriger *********************

resolution()