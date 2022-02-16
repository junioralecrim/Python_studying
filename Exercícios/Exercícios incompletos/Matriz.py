lista1 = []
lista2 = []
lista3 = []

matriz = [lista1] + [lista2] + [lista3]

cont = 0

for i in range(3):
    if(cont < 3):
        lista1[i] = input("Digite o %d° valor: " % (cont + 1))
        cont += +1

#        if (cont > 3) and (cont < 6):

print(matriz)

# https://pt.stackoverflow.com/questions/91908/como-obter-a-linha-de-um-determinado-indice-de-matriz-python