'''Uma loja oferece frete grátis apenas para compras acima de R$150.

Receba o valor da compra.

Exiba:

"Frete grátis" para compras acima de R$150.
"Frete cobrado" para os demais casos.'''

valor = int(input('Informe o valor da compra: '))
if valor > 150:
    print('Frete grátis')
else:
    print('Você não tem direito a frete grátis')