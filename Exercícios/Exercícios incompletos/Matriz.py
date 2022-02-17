lista1 = []
lista2 = []
lista3 = []
listaAux = []
cont = 0

for i in range(9):
    if(cont < 3):
        e = input("Digite o %d° valor: " % (cont + 1))
        listaAux.append(e)
        cont += +1
        

    if((cont >= 3) and (cont < 6)):
        e = input("Digite o %d° valor: " % (cont + 1))
        listaAux.append(e)
        cont += +1


    if((cont >= 6) and (cont < 9)):
        e = input("Digite o %d° valor: " % (cont + 1))
        listaAux.append(e)        
        cont += +1

listaAux.sort(key=len)
cont = 0

while (cont < 9):
  
    if(cont < 3):
        lista1.append(listaAux[cont])
    
    if((cont >= 3) and (cont < 6)):
        lista2.append(listaAux[cont])

    if((cont >= 6) and (cont < 9)):
        lista3.append(listaAux[cont])

    cont += +1







matriz = [lista1] + [lista2] + [lista3]

#       

print(listaAux)

# https://pt.stackoverflow.com/questions/91908/como-obter-a-linha-de-um-determinado-indice-de-matriz-python

# https://pt.stackoverflow.com/questions/91908/como-obter-a-linha-de-um-determinado-indice-de-matriz-python