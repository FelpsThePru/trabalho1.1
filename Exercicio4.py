#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
# ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
opcao = 's'
while opcao == 's' or opcao == 'S':

    p1 = str(input('Telefonou para Vítima? \nS - Sim?\nN - Não?'))
    p2 = str(input('Esteve no Local do Crime? \nS - Sim?\nN - Não?'))
    p3 = str(input('Mora perto da Vítima? \nS - Sim?\nN - Não?'))
    p4 = str(input('Devia para Vítima? \nS - Sim?\nN - Não?'))
    p5 = str(input('Já trabalhou com a Vítima? \nS - Sim?\nN - Não?'))
    var = 0

    if p1 == 's' or p1 == 'S':
        var = var +1

    if p2 == 's' or p2 == 'S':
        var = var + 1

    if p3 == 's' or p3 == 'S':
        var = var + 1

    if p4 == 's' or p4 == 'S':
        var = var + 1

    if p5 == 's' or p5 == 'S':
        var = var + 1

    if var == 2:
        print('Você é Suspeito.')
    elif var == 3 or var == 4:
        print('Você é Cúmplice.')
    elif var == 5:
        print('Você é o Assassino.')
    else:
        print('Você é Inocente.')

    opcao = str(input('Fazer novamente? \nS - Sim? N - Não?'))
    if opcao == 'n' or opcao == 'N':
        print('Fim do projeto')
