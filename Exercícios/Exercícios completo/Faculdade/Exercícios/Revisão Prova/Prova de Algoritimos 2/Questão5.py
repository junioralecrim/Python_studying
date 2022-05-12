vetor = [23, 1, 9, 7, 3, 11, 13, 15, 8, 12]


def selectionSort(array): #defindo a função sort, passando como parâmetro a lista/vetor

    for index in range(0, len(array)): #o laço for vai percorrer o index (início) até o final do tamanho da lista

        min_index = index #É atribuido a variável min_index o valor da posição em que o laço está (index)

        for right in range(index + 1, len(array)): #Aqui o laço for vai percorrer o vetor a partir do valor da posição seguinte (index+1 = right) do array passado, a partir do index (posição -1 ao do laço)
            if array[right] < array[min_index]: #O if vai fazer a verificação. O valor que o index+1 (rigth) está acessando é menor que o valor atribuído inicialmente ao
                #min_index? Se for...
                min_index = right #o min_index agora recebe o valor do right
                #isso vai acontecendo até o último valor do vetor. Quando o laço "right" termina, vai ocorrer a troca das posições entre os valores.

        array[index], array[min_index] = array[min_index], array[index] #o valor da posição min_index é colocado na posição do index, basicamente os valores aqui são trocados a partir das posições dos mesmos no array.
    return array #ao final de todas as interações, a função retorna o array já ordenado

#NOTAS: "right" quer dizer que eu estou acessando o valor à direita do valor que estou usando para comparação, e vai seguindo com os demais valores à direita

vetor = selectionSort(vetor)

print(vetor)