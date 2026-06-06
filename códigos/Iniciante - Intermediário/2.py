'''Um aquário de peixes ornamentais deve permanecer entre 24°C e 28°C.
Receba a temperatura atual da água e informe:
"Temperatura ideal" se estiver na faixa.
"Água muito fria" se estiver abaixo de 24°C.
"Água muito quente" se estiver acima de 28°C.'''

temperatura = int(input('Informe a temperatura: '))
if temperatura < 24:
    print('Água muito fria')
elif temperatura > 28:
    print('Água muito quente')
elif 24 < temperatura < 28:
    print('Temperatura ideal')