'''Um parque de diversões oferece descontos conforme a idade:

Menores de 12 anos → 50% de desconto
Entre 12 e 59 anos → sem desconto
60 anos ou mais → 30% de desconto

Receba:

Idade
Valor do ingresso

Calcule e exiba o valor final a ser pago.'''

valor = 50
idade = int(input('Informe sua idade: '))
if idade < 12:
    valor = valor-(valor* 0.5)
    print(f'Você tem 50% de descont. O valor do ingresso é: {valor}')
elif idade >= 60:
    valor = valor-(valor * 0.3)
    print(f'Você tem 30% de desconto. O valor do ingresso é: {valor}')
else:
    print('Você não tem direito a desconto')