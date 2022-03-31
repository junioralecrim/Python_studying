#selection sort
#Passo a passo:
# 1° Descobrir o menor item da lista
# 2° colocar dentro de uma função





lista = [7, 5, 1, 3, 8]
n = len(lista)
minimo = lista[0]

for i in range(n):
    if(lista[i]< minimo):
        minimo = lista[i]


        

print(lista)