# 1°) algoritimo que faz a conversão do kelvin para grau célcius
# 2) Pedir pro usuário dizer a temperatura e devolver o estado físico 
# Hg (mercurio) >= -38,8 (sólido) 
# Hg < 38,8 e 1538°C (líquido)
# Hg 1538°C (Gasoso)
# Hg 10.000° (Plasma)
# Hg -273,14° (Condensado de Bosen)



#1
valor = float(input("Digite qual a temperatura do Mercúrio (em °C) para obter seu estado físico e a temperatura em Kelvin: "))

if (valor <= -38.8) and (valor >= -273.14):
    estadoMercurio = 'Sólido'
if (valor <= -273.14):
    estadoMercurio = 'Condensado de Bosen'
if (valor >= 38.8) and (valor < 1538):
    estadoMercurio = 'Líquido'
if (valor > 1538) and (valor < 10000):
    estadoMercurio = 'Plasma'

convertido = valor + 273

print(f"A temperatura do mercúrio em °C é de {valor}, está no estado físico {estadoMercurio} e sua temperatura em Kelvin é de {convertido}")

 
