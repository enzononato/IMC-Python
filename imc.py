def calculoIMC(pesoObtido, alturaObtida):
    resultBMI = pesoObtido / alturaObtida**2
    print('Seu IMC: {}'.format(resultBMI))

weight = float(input('Qual o seu peso (em Kg)? '))
height = float(input('qual a sua altura (em metros)? '))

calculoIMC (weight, height)