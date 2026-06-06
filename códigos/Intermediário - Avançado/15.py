'''Uma livraria possui a seguinte promoção:
Compras acima de R$100 → 10% de desconto.
Compras acima de R$200 → 20% de desconto.
Clientes VIP recebem mais 5% de desconto adicional.
Receba:
Valor da compra.
Se é VIP (S ou N).
Calcule o desconto total e o valor final.'''

valor = int(input('Informe o valor da sua compra: '))
vip = input('Você é VIP? (S ou N): ')

if valor > 100:
    valor = valor-(valor*0.1)
    print(f'Valor com desconto: {valor}')
    if vip == 'S':
        valor = valor-(valor*0.05)
        print(f'Valor com 5% adicional: {valor}')
elif valor > 200:
    valor=valor-(valor*0.2)
    print(f'Valor com desconto: {valor}')
    if vip == 'S':
        valor = valor-(valor*0.05)
        print(f'Valor com 5% adicional: {valor}')