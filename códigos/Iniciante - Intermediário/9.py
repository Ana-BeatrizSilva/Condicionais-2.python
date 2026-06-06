'''Uma empresa utiliza drones para entregas.

Para uma entrega ser autorizada:

O peso do pacote deve ser de no máximo 5 kg.
A velocidade do vento deve ser menor ou igual a 30 km/h.

Receba:

Peso do pacote
Velocidade do vento

Informe:

"Entrega autorizada"
"Peso excedido"
"Vento acima do permitido"
"Peso e vento fora dos limites"'''

peso = int(input('Informe o peso do pacote: '))
velocidade = int(input('Informe a velocidade do vento: '))

if peso <= 5 and velocidade <= 30:
    print('Entrega autorizada')
elif peso > 5:
    print('Peso excedido')
elif velocidade > 30:
    print('Vento acima do permitido')
elif peso > 5 and velocidade > 30:
    print('Vento e velocidade maiores que o permitido')