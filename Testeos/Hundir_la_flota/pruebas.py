import numpy as np
import random
from main import*

class Tablero:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño

    def tablero_player1(self, tamaño):
        tablero1 = np.full((tamaño, tamaño), " ")
        return tablero1

    def tablero_player2(self, tamaño):
        tablero2 = np.full((tamaño, tamaño), " ")
        return tablero2

class Barco:
    
    barcos = [[(0,1), (4, 3), (8, 8), (7, 1)],
              [(2,2), (2,1), (5,6), (4,6), (9,6), (9,5)],
              [( 9,1), (9,2), (9,3), (0,7), (1,7), (2,7)],
              [(7,3), (7,4), (7,5), (7,6)]]

    def coloca_barco(self, tablero):
        for barco in self.barcos:
            for pieza in barco:
                tablero[pieza] = "O"
        return tablero
    
    def crea_barco_aleatorio(self, tablero, nombre):
        longitud = nombre.longitud
        fila = random.randint(0,9)
        columna = random.randint(0,9)
        orientacion = random.choice(["N", "S", "E", "O"])
        if orientacion == "N": 
            if fila - longitud >= 0: 