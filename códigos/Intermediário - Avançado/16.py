'''Um banco avalia pedidos de empréstimo usando:
Aprovação automática
Score ≥ 800
Renda ≥ R$4.000
Análise manual
Score entre 600 e 799
Reprovação
Score abaixo de 600
Contudo:
Se o cliente possuir dívida ativa, o resultado deve ser:
Empréstimo negado
independentemente dos outros critérios.
Receba:
Score
Renda
Possui dívida ativa? (S ou N)'''

score = int(input('Informe o seu score: '))
renda = int(input('Informe sua renda: '))
divida = input('Possui dívida ativa?: ').upper()

if divida == 'S':
    print('Empréstimo NEGADO')
else:
    if score >= 800 and renda >= 4000:
        print('APROVADO!')
    elif 600 <= score <= 799:
        print('Análise manual')
    elif score < 600:
        print('REPROVADO!')