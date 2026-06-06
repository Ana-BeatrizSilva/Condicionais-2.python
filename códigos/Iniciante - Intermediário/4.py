'''Uma corrida beneficente classifica os participantes de acordo com o tempo concluído:

Até 30 minutos → Ouro
Até 45 minutos → Prata
Até 60 minutos → Bronze
Acima disso → Participação

Receba o tempo do corredor e exiba sua categoria.'''

tempo = int(input('Informe o seu tempo: '))
if tempo <= 30:
    print('Ouro')
elif tempo <= 45:
    print('Prata')
elif tempo <= 60:
    print('Bronze')
else:
    print('Participação')