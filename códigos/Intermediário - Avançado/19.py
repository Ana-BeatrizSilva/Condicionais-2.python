'''Um estacionamento cobra:
Até 2 horas → R$8
Até 5 horas → R$15
Até 10 horas → R$25
Acima de 10 horas → R$25 + R$3 por hora excedente
Entretanto:
Se o veículo permanecer mais de 24 horas, deve ser exibido:
Consultar administração
Receba o número de horas estacionado e determine o valor ou a mensagem adequada.'''

horas = int(input('Informe as horas no estacionamento: '))

if horas > 24:
    print('Consultar administração')
elif horas <= 2:
    print('Valor: R$8.00')
elif horas <= 5:
    print('Valor: R$15.00')
elif horas <= 10:
    print('Valor: R$25.00')
else:
    excedente = horas - 10
    valor = 25 + (excedente * 3)
    print(f'Valor: R${valor:.2f}')