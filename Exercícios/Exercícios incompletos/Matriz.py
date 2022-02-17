lista1 = []
lista2 = []
lista3 = []
listaAux = []
cont = 0
cont2 = 0

for i in range(9):
    if(cont < 3):
        e = input("Digite o %d° valor: " % (cont + 1))
        lista1.append(e)
        listaAux.append(e)
        cont += +1
        

    if((cont >= 3) and (cont < 6)):
        e = input("Digite o %d° valor: " % (cont + 1))
        lista2.append(e)
        listaAux.append(e)
        cont += +1


    if((cont >= 6) and (cont < 9)):
        e = input("Digite o %d° valor: " % (cont + 1))
        lista3.append(e)
        listaAux.append(e)
        listaAux = sorted(listaAux)
        
        cont += +1

while (cont2 < 9):
  
  cont2 += +1

  if(cont2 < 3):
    lista1.append(listaAux[+1])
  
  if((cont >= 6) and (cont < 9)):
    lista2 = listaAux[-3]









matriz = [lista1] + [lista2] 

#       

print(lista1)

# https://pt.stackoverflow.com/questions/91908/como-obter-a-linha-de-um-determinado-indice-de-matriz-python

# https://pt.stackoverflow.com/questions/91908/como-obter-a-linha-de-um-determinado-indice-de-matriz-python