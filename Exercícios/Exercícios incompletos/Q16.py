print("----- QUANTIDADE DE LATAS DE TINTA E VALOR TOTAL -----")
area = float(input("Digite a área total a ser pintada em metros quadrados: "))

#divide a quantidade de metros dados por 3, que é a quantidade de litros pra cada 3m (1:3)
quantLitros = area/3
i = 0
contadorLitros = quantLitros
contadorLatas = 0

#trabalhando no caso para caso seja 1 ou maior o número de latas
while (contadorLitros > 0):
    if(quantLitros >= 18):
        i += 1
        contadorLitros += - 18
        contadorLatas += 1
    else:
        contadorLitros += - 18
        contadorLatas += 1



print(f"\nVocê vai precisar de exatamente %.2f litros de tinta\n\nA quantidade de latas mínimas para a pintura é de {contadorLatas} lata" % quantLitros)
