lista = [5, 9, 50, 1, 3, 7, 900, 540]
listaOrdenada = []

def quicksort(A):
    if len(A) == 0:
        return A
    pivo = A[0]
    frente = quicksort([menor for menor in A[1:] if menor <= pivo])
    tras = quicksort([maior for maior in A[1:] if maior > pivo])
    return frente + [pivo] + tras

listaOrdenada = quicksort(lista)

print(listaOrdenada)