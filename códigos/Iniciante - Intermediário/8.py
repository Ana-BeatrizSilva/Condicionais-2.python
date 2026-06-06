'''Um aplicativo monitora o nível de combustível de veículos.

Receba a porcentagem do tanque.

Exiba:

"Tanque cheio" → acima de 75%
"Nível adequado" → entre 40% e 75%
"Abasteça em breve" → entre 15% e 39%
"Combustível crítico" → abaixo de 15%'''

tanque = int(input('Informe a porcentagem do tanque: '))
if tanque > 75:
    print('Tanque cheio')
elif 40 <= tanque <= 75:
    print('Nível adequado')
elif 15 <= tanque <= 39:
    print('Abasteça em breve')
elif tanque < 15:
    print('Nível crítico')