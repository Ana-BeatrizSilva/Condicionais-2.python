'''Uma instituição concede bolsas segundo as seguintes regras:

Bolsa Integral
Média ≥ 9
Renda familiar ≤ R$2.000
Bolsa Parcial
Média ≥ 7
Renda familiar ≤ R$4.000
Sem bolsa
Todos os demais casos

Receba:

Média do aluno
Renda familiar

Informe o benefício obtido.'''

media = int(input('Informe sua média: '))
renda = float(input('Informe sua renda: '))

if media >= 9 and renda <= 2000.00:
    print('Bolsa Integral')
elif media >= 7 and renda <= 4000.00:
    print('Bolsa Parcial')
else:
    print('Sem direito a bolsa')