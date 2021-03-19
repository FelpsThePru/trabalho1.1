#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.
n1 = float(input('Informe um Número: '))
n2 = float(input('Informe outro Número: '))

opcao = str(input('Informe uma Operação \n( + )Soma \n( - ) Subtração \n( * ) Multiplicação \n( / ) Divisão '))

resultado = 0

if opcao == '+':
    resultado = n1 + n2
    print(f'O valor da Soma é= {resultado}')

elif opcao == '-':
    resultado = n1 - n2
    print(f'O valor da Subtração é= {resultado}')

elif opcao == '*':
    resultado  = n1 * n2
    print(f'O valor da Multiplicação é= {resultado}')

elif opcao == '/':
    resultado = n1 / n2
    print(f'O valor da Divisão é= {resultado}')
else:
    print('Opção Invalida...')

if resultado % 2 == 0:
    print('O número é Par.')
else:
    print('O número é Impar.')

if resultado // 1 == resultado:
    print('O número é Inteiro.')
else:
    print('O número é Decimal.')

if resultado < 0:
    print('O número é Negativo.')
else:
    print('O número é Positivo.')