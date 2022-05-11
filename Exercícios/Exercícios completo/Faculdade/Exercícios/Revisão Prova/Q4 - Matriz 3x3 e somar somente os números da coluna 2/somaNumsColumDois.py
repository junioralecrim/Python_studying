
linha1 = []
linha2 = []
linha3 = []
soma = 0


for i in range(0, 9):
   num = int(input(f"Digite o {i+1}° número da matriz: "))
   if(i<3):
       linha1.append(num)
       if(i==1):
           soma += num
   if(i>=3) and (i<6):
       linha2.append(num)
       if (i == 4):
           soma += num
   if(i >= 6) and (i < 9):
       linha3.append(num)
       if (i == 7):
           soma += num


print(f"Linha 1: {linha1}\nLinha 2: {linha2}\nLinha 3: {linha3}")
matriz = [linha1] + [linha2] + [linha3]

print(f"Matriz: {matriz}")

print(soma)
