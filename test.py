
import numpy as np


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
                        #print("trying n = ", n , "at position y = ", y+1 , "and x = ", x+1)
                        #print(np.array(grille))
                        resolution()
                        #print("resetting to 0", "at position y = ", y+1 , "and x = ", x+1)
                        grille[y][x] = 0
                        #print(np.array(grille))
                return
    print(np.array(grille))
    input("Jouer encore une fois ?")

resolution()