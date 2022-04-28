def fat(x):
    if x == 1 or x == 0:
        return x
    elif x<0:
        return("Não é possível pois o número é negativo")
    else:
        return x*fat(x-1)

x = int(input("Digite um número: "))

print(fat(x))