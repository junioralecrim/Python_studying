linha1 = []
linha2 = []
linha3 = []
linha4 = []

for i in range(16):
   aux = int(input(f"Digite o {i+1}° número: "))
   if(i<4):
       linha1.append(aux)
   if(i >= 4) and (i<8):
       linha2.append(aux)
   if(i >= 8) and (i<12):
       linha3.append(aux)
   if(i >= 12) and (i<16):
       linha4.append(aux)

matriz = [linha1] + [linha2] + [linha3] + [linha4]

print(matriz)
