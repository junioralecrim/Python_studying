num = int(input("Digite um número e direi se é primo ou não:"))

cond = 2

for c in range(1, num + 1):
    if num % c == 0:
        cond += 1

if cond == 4:
    print("É número primo")
else:
    print("Não é número primo")