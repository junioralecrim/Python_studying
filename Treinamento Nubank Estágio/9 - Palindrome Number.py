num = int(input("Digite um número qualquer para verificar se este é um palíndromo ou não: "))

lista = []
listaInvert = []
ultimoAlg = 0


while(num > 0):
    ultimoAlg = num % 10
    listaInvert.append(int(ultimoAlg))
    lista.insert(0, int(ultimoAlg))
    num = (num - ultimoAlg)/10

for i in range(len(lista)):
    if lista[i] == listaInvert[i]:
        result = True
    else:
        result = False
        break



print(lista, listaInvert, result)


