#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
opcao = 's'
while opcao in 'sS':
    print('Bem-Vindo ao Posto Sapão, oque vai ser xará?')
    Combustivel = input('Tipo de Combustível: A - Álcool   G - Gasolina  S - Sair(Exit)')

    if Combustivel in 'aAGg':
        litros = float(input('Informe Quantos Litros: '))

        #------------------Álcool-------------------
        if Combustivel in 'aA':
            print('-----------------------------')
            #Desconto de 3%
            if litros <= 20:
                ValorComb = litros * 1.90
                ValorDesc = ValorComb - (ValorComb * 3) / 100
                print(f'Litros de Alcool: {litros} \nVlrUni R$: 1.90 \nValor Total R$: {ValorComb} \nValor Total com Desconto R$: {ValorDesc}')

            #Desconto de 5%
            else:
                ValorComb = litros * 1.90
                ValorDesc = ValorComb - (ValorComb * 5) / 100
                print(f'Litros de Alcool: {litros} \nVlrUni R$: 1.90 \nValor Total R$: {ValorComb} \nValor Total com Desconto R$: {ValorDesc}')

        #--------------------Gasolina---------------------
        else:
            print('-----------------------------')
            #Desconto de 4%
            if litros <= 20:
                ValorComb = litros * 2.50
                valorDesc = ValorComb - (ValorComb * 4) / 100
                print(f'Litros de Gasolina: {litros} \nVlrUni R$: 2.50 \nValor Total R$: {ValorComb} \nValor Total com Desconto R$: {valorDesc}')

            #Desconto de 6%
            else:
                valor = litros * 2.50
                valorDesc = ValorComb - (ValorComb * 6) / 100
                print(f'Litros de Gasolina: {litros} \nVlrUni R$: 2.50 \nValor Total R$: {ValorComb} \nValor Total com Desconto R$: {ValorDesc}')

    elif Combustivel in 'sS':
        print('Finalizando...')
        break

    else:
        print('Opção Inválida...')