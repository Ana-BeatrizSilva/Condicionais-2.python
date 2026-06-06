'''Uma biblioteca escolar permite empréstimos apenas para alunos que não possuem multas pendentes.
O programa deve receber:
Nome do aluno
Quantidade de multas pendentes
Exiba:
"Empréstimo autorizado" se não houver multas.
"Regularize sua situação antes de pegar livros" caso contrário.'''

nome = input('Informe seu nome: ')
print(f'Olá, {nome}')
multas = int(input('Informe a quantidade de multas: '))

if multas == 0:
    print('Empréstimo autorizado')
else:
    print('Regularize sua situação antes de pegar livros')