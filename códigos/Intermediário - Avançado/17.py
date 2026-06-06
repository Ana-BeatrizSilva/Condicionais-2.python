'''Uma residência possui um sistema inteligente.
Receba:
Produção de energia (kWh)
Consumo de energia (kWh)
Situações:
Produção maior que consumo → Excedente
Produção igual ao consumo → Equilíbrio
Produção menor que consumo → Déficit
Além disso:
Se o déficit ultrapassar 50 kWh, exiba também:
Consumo crítico'''

producao = int(input('Informe a produção de energia: '))
consumo = int(input('Informe o consumo de energia: '))

if producao > consumo:
    print('Excedente')
elif producao == consumo:
    print('Equilíbrio')
elif producao < consumo:
    print('Déficit')
    if consumo - producao > 50:
        print('Consumo crítico')