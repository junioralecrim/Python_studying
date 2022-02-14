idadeGeral, contadorGeral, contadorHomens, idadeHomens, contadorMulheres, idadeMulheres  = 0, 0, 0, 0, 0, 0

#leitura e processamento de dadods
for i in range(10):
    print("%d° pessoa" % (contadorGeral + 1) )
    sexo = input("\nDigite seu sexo ('M' para mulher e 'H' para homem): ")
    sexo = sexo.upper()
    idade = float(input("\nDigite sua idade: "))
    
    if (sexo == 'M'):
        idadeMulheres += idade
        contadorMulheres += +1

    if (sexo == 'H'):
        idadeHomens += idade
        contadorHomens += +1

    if ((sexo == 'M') or (sexo == 'H')):
        idadeGeral += idade
        contadorGeral += +1

#exibição de dados 

print("\n------- Mulheres -------\n")
print("Quantidade de mulheres: %d" % contadorMulheres)
print("Média de idade das mulheres: %.2f\n" % (idadeMulheres/contadorMulheres))

print("\n------- Homens -------\n")
print("Quantidade de homens: %d" % contadorHomens)
print("Média de idade das homens: %.2f\n" % (idadeHomens/contadorHomens))

print("\n------- Geral -------\n")
print("Quantidade de homens: %d" % contadorGeral)
print("Média de idade das homens: %.2f\n" % (idadeGeral/contadorGeral))

    


        

    
