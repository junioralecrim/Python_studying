lista1 = []
lista2 = []
lista3 = []
listaAux = []
listaÍmpares = []
cont = 0
acumulador = 0

for i in range(9): #receber os valores
    e = int(input("Digite o %d° valor: " % (cont + 1)))
    listaAux.append(e)
    cont += +1
    
    if (e%2 != 0):
        acumulador += e
        listaÍmpares.append(e)


cont = 0




while (cont < 9): #separar os valores em cada linha/coluna da matriz 3x3  
    if(cont < 3):
        lista1.append(listaAux[cont])
    
    if((cont >= 3) and (cont < 6)):
        lista2.append(listaAux[cont])

    if((cont >= 6) and (cont < 9)):
        lista3.append(listaAux[cont])

    cont += +1


matriz = [lista1] + [lista2] + [lista3]
print(matriz)

print("\nOs números ímpares digitados pelo usuário foram: ")
print(listaÍmpares)

print("\nA soma de todos os números ímpares é: %d" % (acumulador))
