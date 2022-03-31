#selection sort
#Passo a passo:
# 1° Descobrir o menor item da lista
# 2° colocar dentro de uma função

#Rascunho do algoritimo de ordenação para mudar as posições
#        if (lista[2] < minimo):    
 #           aux = lista[0]
  #          minimo = lista[2]
   #         lista[2] = aux


lista = [7, 5, 1, 3, 8]
n = len(lista)
minimo = lista[0]

for i in range(n):
    if(lista[i]< minimo):
        minimo = lista[i]
    
    for j in range(n):


        

print(lista)
