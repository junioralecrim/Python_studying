num = (input("Digite um número romano qualquer para obter seu equivalente numérico: "))
num = num.upper()
soma = 0
aux = 0

romanNumber = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for i in range(len(num)):
    aux = i + 1
    # verificando se o se a letra existe no dicionário
    if num[i] in romanNumber: #se existir, o código continua     if num[i] in romanNumber: #se existir, o código continua
        if romanNumber[num[i]] >= romanNumber[num[aux]] and i < len(num) - 1:
            print(i)
