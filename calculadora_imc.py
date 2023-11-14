peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = round(peso / (altura * altura), 2)
print("Seu IMC é:" f"{imc}")

if imc < 16:
    print("Sua classificação é Magreza grave")
elif (imc >= 16) and (imc < 17):
    print("Sua classificação é Magreza moderada")
elif (imc >= 17) and (imc < 18.5):
    print("Sua classificação é Magreza leve")
elif (imc >= 18.5) and (imc < 25):
    print("Sua classificação é Saudável")
elif (imc >= 25) and (imc < 30):
    print("Sua classificação é Sobrepeso")
elif (imc >= 30) and (imc < 35):
    print("Sua classificação é Obesidade Grau I")
elif (imc >= 35) and (imc < 40):
    print("Sua classificação é Obesidade Grau II")
else:
    print("Sua classificação é Obesidade Grau III")
