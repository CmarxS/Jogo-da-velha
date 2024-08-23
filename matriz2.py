matriz = []
for _ in range(4):
    matriz.append([0]*5)

num = 1
for linha in range(4):
    for col in range(5):
        matriz[linha][col] = num  
        num += 1

for a in matriz:
    print(a)