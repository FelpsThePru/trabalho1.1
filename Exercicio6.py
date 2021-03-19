#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler
# a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
sistema = 'P'
while sistema in 'pP':
    print('Bem Vindo a Frutaria Sapao')
    sistema = input(' P - Próximo  S - Sair(Exit)')

    if sistema in 'pP':
        morango = float(input('Informe Quantos Kg de Morango você quer: '))
        maca = float(input('Informe Quantos Kg de Maçã você quer: '))

        kgFrutas = morango + maca

        if morango <= 5:
            print('-------------------------------------------')
            valorMorango = morango * 2.5
            print(f'Quantidade Morango Kg: {morango}\nValor Kg R$: 2.50 \nValor Total R$: {valorMorango:.2f}')
        else:
            print('-------------------------------------------')
            valorMorango = morango * 2.20
            print(f'Quantidade Morango Kg: {morango}\nValor Kg R$: 2.20 \nValor Total R$: {valorMorango:.2f}')

        if maca <= 5:
            print('-------------------------------------------')
            valorMaca = maca * 1.80
            print(f'Quantidade Maçã Kg: {maca}\nValor do Kg R$: 1.80 \nValor Total Maçã R$: {valorMaca:.2f}')
        else:
            print('-------------------------------------------')
            valorMaca = maca * 1.50
            print(f'Quantidade Maçã Kg: {maca}\nValor do Kg R$: 1.5 \nValor Total Maçã R$: {valorMaca:.2f}')

        valorTotal = valorMaca + valorMorango
        print('-------------------------------------------')
        print(f'Valor Total da Compra R$: {valorTotal:.2f}')
        if kgFrutas > 8 or valorTotal > 25:
            valorDesconto = valorTotal - (valorTotal * 10) / 100
            print(f'Valor com Desconto Incluso: {valorDesconto:.2f}')
        print('-------------------------------------------')


    elif sistema in 'sS':
        print('-------------------------------------------')
        print('Volte Sempre, até a próxima ツ')
        break