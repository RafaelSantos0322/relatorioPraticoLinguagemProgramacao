import math 

# Começamos dando mensagem de Boas vindas Ao Usuário
print("Bem-vind@ a calculadora de IMC(Índice de Massa Corpórea)")

# Logo após criamos as váriaveis que irão receber os dados dígitados pelo usuário
peso = float(input("Para começar digite seu peso  "))
altura = float(input("Agora digite sua altura ex.: 2.10 "))

# Aqui fazemos o  tratamamtento dos valores digitados verificando se é maior que 0
if peso > 0 and altura > 0:
     imc = peso / ( math.pow(altura, 2)) 
     
# Criamos uma váriavel níveis que recebe um array com níveis de peso
niveis = ["Magresa Grave", "Magresa Moderada", "Magresa Leve", "Peso Normal", "Sobrepeso", "Obesidade Grau I", "Obesidade Grau II", "Obesidade Morbida"]

#  Criamos uma váriavel que formata o  texto de acordo com seu imc e nível
textoFormatado = f"Baseado no seu IMC de {round(imc, 2)} você está no nivel "

# Aqui fazemos a verificação através de estruturas de controle para determinar em qual nível a pessoa está enquadrada
if imc < 16:
     print( textoFormatado + niveis[0] )
     print("Procure um médico!")
elif imc < 17:
     print(textoFormatado + niveis[1])
     print("Procure um médico!")
elif imc < 18.5:
     print(textoFormatado + niveis[2])
     print("Você está quase lá, busque se alimentar mais!")
elif imc < 25:
     print(textoFormatado + niveis[3])
     print("Parabéns!")
elif imc < 30:
      print(textoFormatado + niveis[4])
      print("CUIDADO!!! Busque melhorar sua alimentação e pratique mais exercícios")
elif imc < 35:
      print(textoFormatado + niveis[5])
      print("CUIDADO!!! Busque um médico ou nutricionista e mude seu estilo de vida")
elif imc < 40:
      print(textoFormatado + niveis[6])
      print("CUIDADO!!! Busque um médico ou nutricionista rapidamente")
elif imc > 40:
      print(textoFormatado + niveis[7])
      print("CUIDADO!!! Busque um médico ou nutricionista rapidamente")

