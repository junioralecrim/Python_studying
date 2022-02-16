contPosição = 0
mat = [[0 for _ in range(3)]for _ in range(3)]
matOrdenado = [[0 for _ in range(3)]for _ in range(3)]
aux = []
cont = 0
n = 1

for i in range(3):
    for j in range(3):
        mat[i][j] = input("Digite o valor %d°: " % (contPosição+1))
        contPosição += +1

        if(contPosição <= 3):
            aux += mat[i][j]
            matOrdenado = sorted(aux)
            
        if((contPosição > 3) and (contPosição <= 6)):
            aux += mat[i][j]
            matOrdenado = sorted(aux)


print(matOrdenado)
