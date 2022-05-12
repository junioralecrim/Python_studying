numTabuada = int(input("Digite o número do qual você deseja montar a tabubada: "))
numInicio = int(input("Digite o número do qual você deseja iniciar a tabubada: "))
numFinal = int(input("Digite o número do qual você deseja finalizar a tabubada: "))


print(f"\nMontando a tabuada do {numTabuada}, começando em {numInicio} e terminando em {numFinal}\n")
for i in range(numInicio, numFinal+1):
    print(f"{numTabuada} x {i} = {numTabuada*i}")
