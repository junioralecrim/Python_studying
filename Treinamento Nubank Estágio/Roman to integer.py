numRoman = (input("Digite um número romano qualquer para obter seu equivalente numérico: "))
numRoman = numRoman.upper()

romanNumber = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for i in range(1, 6):
    print(romanNumber[i])




