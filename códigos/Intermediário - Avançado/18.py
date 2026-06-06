'''Um atleta só pode competir se:
Idade entre 16 e 40 anos.
Possuir atestado médico válido.
Após ser aprovado, ele é classificado:
Até 18 anos → Júnior
Até 30 anos → Adulto
Acima disso → Master
Receba:
Idade
Possui atestado? (S ou N)
Determine se ele pode competir e, em caso positivo, sua categoria.'''

idade = int(input('Informe sua idade: '))
atestado = input('Possui atestado? (S ou N): ')

if 16<= idade <= 60 and atestado == 'S':
    print('Aprovado para competição')
    if idade <= 18:
        print('Classificação: Júnior')
    elif idade <= 30:
        print('Classificação: Adulto')
    elif idade > 30:
        print('Classificação: Master')
else:
    print('Reprovado')