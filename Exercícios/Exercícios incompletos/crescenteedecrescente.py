#Ler do teclado uma lista com 5 inteiros e imprimir True se a lista estiver ordenada de forma crescente ou False caso contrário.

#recebendo valores
valoresNormais = []
for i in range(5):
    e = input("Digite o %d° valor: " % (i+1))
    valoresNormais.append(e) #quando usado o append a lista não imprime de forma separada os números com mais de um algarismo.
    
valoresOrdenados = sorted(valoresNormais)

#verificação
if (valoresNormais == valoresOrdenados):
    print("A lista está ordenada de forma ascendente:", valoresNormais)
else:
    print("\nA lista está ordenada de forma decrescente ou aleatória.")
