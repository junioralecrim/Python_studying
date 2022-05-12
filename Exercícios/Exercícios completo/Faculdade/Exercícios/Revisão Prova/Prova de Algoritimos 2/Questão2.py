x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
soma = 0


for i in range(x+1, y):
    if(i%2 != 0):
        soma += + i
        print(f"Números ímpares entre o primeiro e segundo número: {i}")

print(f"\nX: {x}\nY: {y}\nResultado de saída: {soma}")

