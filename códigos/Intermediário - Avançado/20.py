'''Um hospital realiza uma triagem inicial.
Receba:
Temperatura corporal
Frequência cardíaca
Saturação de oxigênio
Classificação:
Emergência
Se qualquer uma das condições ocorrer:
Saturação abaixo de 90%
Temperatura acima de 40°C
Frequência cardíaca acima de 140 bpm
Urgente
Se qualquer uma ocorrer:
Saturação entre 90% e 94%
Temperatura entre 38°C e 40°C
Frequência cardíaca entre 110 e 140 bpm
Estável
Todos os demais casos.
Exiba a classificação final.'''

temperatura = int(input('Informe a temperatura: '))
frequencia = int(input('Informe a frequência cardíaca: '))
saturacao = int(input('Informe a saturação de oxigênio: '))

if saturacao < 90 or temperatura > 40 or frequencia > 140:
    print('Emergência')
elif 90 <= saturacao <= 94:
    print('Urgente')
elif 38 <= temperatura <= 40:
    print('Urgente')
elif 110 <= frequencia <= 140:
    print('Urgente')
else:
    print('Estável')