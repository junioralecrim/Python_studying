num = (input("Digite um número romano qualquer para obter seu equivalente numérico: "))
num = num.upper()
aux = 0

romanNumber = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for i in range(len(num)):
    #procurar número de ocorrências das letras i, x, c e m. Só pode ser maior ou igual a 3.
    aux += romanNumber[num[i]]


print(soma)