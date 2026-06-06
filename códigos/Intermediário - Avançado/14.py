'''Um laboratório químico possui as seguintes regras:
O funcionário só pode entrar se:
Possuir crachá válido.
Estiver usando equipamento de proteção.
Tiver concluído o treinamento obrigatório.
Receba três respostas (S ou N).
Informe:
"Acesso liberado"
Ou exatamente quais requisitos estão faltando.'''

possui_cracha = False
possui_equipamento = False
possui_treinamento = False

cracha = input('Possui crachá válido? (S ou N): ')
if cracha == 'S':
    possui_cracha = True

equipamento = input('Possui equipamento? (S ou N): ')
if equipamento == 'S':
    possui_equipamento = True

treinamento = input('Possui treinamento? (S ou N): ')
if treinamento == 's':
    possui_treinamento = True

if possui_cracha == True and possui_equipamento == True and possui_treinamento == True:
    print('Acesso liebrado')
elif possui_cracha == False:
    print('Acesso negado devido a falta do crachá')
elif possui_equipamento == False:
    print('Acesso negado devido a falta do equipamento')
elif possui_treinamento == False:
    print('Acesso negado devido a falta de equipamento')