lista = []

for x in range(8):
    n = int(input("Digite um número inteiro: "))

    inseriu = False
    for i in range(len(lista)):
        if n<lista[i]:
            lista.insert(i, n)
            inseriu = True
            break

    if not inseriu:
        lista.append(n)
        
    print(lista)