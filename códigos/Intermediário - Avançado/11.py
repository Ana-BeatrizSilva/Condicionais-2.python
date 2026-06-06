'''Uma companhia aérea possui as seguintes regras para bagagem de mão:

Peso máximo: 10 kg
Altura máxima: 55 cm
Largura máxima: 35 cm
Profundidade máxima: 25 cm

Receba as quatro informações.

Exiba:

"Bagagem aprovada" se cumprir todos os requisitos.
Caso contrário, informe quais critérios foram violados.'''

peso = int(input('Informe o peso: '))
altura = int(input('Informe a altura: '))
largura = int(input('Informe a largura: '))
profundidade = int(input('Informe a profundidade: '))


if peso <= 10 and altura <= 55 and largura <= 35 and profundidade <= 25:
    print('Bagagem aprovada!')
elif peso > 10:
    print('Peso excedido')
elif altura > 55:
    print('Altura excedida')
elif largura > 35:
    print('Largura excedida')
elif profundidade > 25:
    print('Profundidade excedida')