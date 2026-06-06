'''Um curso técnico utiliza dois critérios para aprovação:

Média final maior ou igual a 7.
Frequência mínima de 75%.

Receba:

Média final
Frequência (%)

Exiba:

"Aprovado"
"Reprovado por nota"
"Reprovado por frequência"
"Reprovado por nota e frequência"'''

media = float(input('Informe a média final: '))
frequencia = int(input('Informe sua frequência: '))

if media >= 7 and frequencia >= 75:
    print('Aprovado!')
elif media < 7:
    print('Reprovado por média')
elif frequencia < 75:
    print('Reprovado por frequencia')
elif media < 7 and frequencia < 75:
    print('Reprovado por média e frequência')