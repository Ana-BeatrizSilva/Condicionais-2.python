'''Uma cafeteria possui a seguinte promoção:

Compras acima de R$50 ganham um cookie grátis.
Clientes cadastrados acumulam pontos.
Se o cliente for cadastrado e gastar mais de R$100, recebe também um café gratuito.

Receba:

Valor da compra
Se o cliente é cadastrado (S ou N)

Exiba todas as vantagens que ele recebeu.'''

valor =  int(input('Informe o valor da sua compra: '))
cadastrado = False
cadastro = input('Você é cadastrado? (S ou N): ')

if cadastro == 'S':
    cadastrado = True
else:
    cadastrado = False

if valor > 50:
    print('Você ganhou um cookie grátis')
elif valor > 100 and cadastrado == True:
    print('Você ganhou um café gratuito')
else:
    print('Você não ganhou nada')