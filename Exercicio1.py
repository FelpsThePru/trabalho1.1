#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
numero = int(input('Digite um número para ver se ele é par ou ímpar: '))

if (numero%2) == 0:
    print("Este número é Par")
else:
    print("Este número é Ímpar")
