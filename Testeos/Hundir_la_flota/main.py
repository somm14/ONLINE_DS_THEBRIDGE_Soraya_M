from pruebas import*

tablero1 = Tablero(10) 
tablero1 = tablero1.tablero_player1(10)


tablero2 = Tablero(10)
tablero2.tablero_player2(10)

barcos = Barco()

tablero1 = barcos.coloca_barco(tablero1)

tablero2 = Tablero(10)
tablero2.tablero_player2(10)

barcos_player2 = [
    Barco("barco1", 1),
    Barco("barco2", 1),
    Barco("barco3", 1),
    Barco("barco4", 1),
    Barco("barco5", 2),
    Barco("barco6", 2),
    Barco("barco7", 2),
    Barco("barco8", 3),
    Barco("barco9", 3),
    Barco("barco10", 4)
]

tablero2 = barcos_player2.crea_barco_aleatorio(tablero2, "barco1")
tablero2 = barcos_player2.crea_barco_aleatorio(tablero2, "barco2")
tablero2 = barcos_player2.crea_barco_aleatorio(tablero2, "barco3")
tablero2 = barcos_player2.crea_barco_aleatorio(tablero2, "barco4")
tablero2 = barcos_player2.crea_barco_aleatorio(tablero2, "barco5")
tablero2 = barcos_player2.crea_barco_aleatorio(tablero2, "barco6")
tablero2 = barcos_player2.crea_barco_aleatorio(tablero2, "barco7")
tablero2 = barcos_player2.crea_barco_aleatorio(tablero2, "barco8")
tablero2 = barcos_player2.crea_barco_aleatorio(tablero2, "barco9")
tablero2 = barcos_player2.crea_barco_aleatorio(tablero2, "barco10")

print(tablero2)