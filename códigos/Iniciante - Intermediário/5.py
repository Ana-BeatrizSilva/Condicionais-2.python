'''.Um sistema exige que a senha:

Tenha pelo menos 8 caracteres.
Não seja exatamente "12345678".

Receba uma senha e informe:

"Senha aceita"
"Senha inválida"

Utilize condicionais e a função len()'''

senha = input('Informe a senha: ')
if len(senha) == 8 and senha != '12345678':
    print('Senha VÁLIDA')
else:
    print('Senha INVÁLIDA')