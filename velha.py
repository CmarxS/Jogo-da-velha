def temEspaco(matriz):
    for lin in range(4):
        for col in range(5):
            if matriz[lin][col] == 0:
                return True
    return False 

def joga(matriz, lin, col, jogador):
    if matriz[lin][col] == 0:
        matriz[lin][col] = jogador