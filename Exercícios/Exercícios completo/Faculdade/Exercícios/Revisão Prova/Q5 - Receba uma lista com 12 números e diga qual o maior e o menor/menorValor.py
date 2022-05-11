def buscarMenor(lst):
    i = float("inf")
    for nr in lst:
        if nr < i:
            i = nr
    return i


lista = []

tamanho = int(input("Diga qual o tamanho da lista:"))

for i in range(tamanho):
    num = int(input(f"{i+1} número: "))
    lista.append(num)

num = buscarMenor(lista)

print(num)