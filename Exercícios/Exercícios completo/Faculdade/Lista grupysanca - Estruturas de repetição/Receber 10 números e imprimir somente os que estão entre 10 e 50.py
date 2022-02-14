valoresNoRange = []

for i in range(10):
    e = int(input("Digite o %d valor: " % (i+1)))
    
    if((e >= 10 ) and (e <= 50)):
        valoresNoRange.append(e)

print("\nValores digitados que estão entre 10 e 50:", valoresNoRange)