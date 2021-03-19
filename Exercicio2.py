#Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
num = float(input ('Digite um número para ver se ele é Decimal ou Inteiro:'))

if int(num) == num:
    print (" Este Número é Inteiro")
else:
    print ("Este Número é Decimal")