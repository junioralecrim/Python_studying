lista = []
listaOrdenada = []
menorValor = 0
maiorValor = 0
posicaoMaiorValor = 0
posicaoMenorValor = 0

for x in range(8):

    n = int(input("Digite um número: "))
    lista.append(n)
    inseriu = False
    
    for i in range(len(listaOrdenada)):
        if n<listaOrdenada[i]:
            listaOrdenada.insert(i, n)
            inseriu = True
            break

    if not inseriu:
        listaOrdenada.append(n)
    print(lista)


#descobrindo o menor valor na lista
maiorValor = listaOrdenada[7]
menorValor = listaOrdenada[0]

print(maiorValor)
print(menorValor)

i = 0

while(i < 8):
    if(lista[i] == menorValor):
        posicaoMenorValor = i
        i += 1
    if(lista[i] == maiorValor):
        posicaoMaiorValor = i
        i += 1
    i += 1