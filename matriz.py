i = 0
tabuleiro = []
while i < 3:
    tabuleiro.append([''] * 3)
    i += 1
tabuleiro[0][2] = "x"
tabuleiro[1][1] = "x"
tabuleiro[1][0] = "o"
tabuleiro[2][0] = "o"

for linha in tabuleiro:
    print(linha)