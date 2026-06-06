'''Um servidor envia alertas conforme seu uso de CPU.
Até 60% → Normal
Acima de 60% até 80% → Atenção
Acima de 80% até 95% → Crítico
Acima de 95% → Emergência
Entretanto:
Se a temperatura do processador estiver acima de 90°C, o status deve ser automaticamente considerado Emergência, independentemente do uso da CPU.
Receba:
Uso da CPU
Temperatura
Determine o status final.'''

cpu = int(input('Informe a porcentagem de uso da CPU: '))
temperatura = int(input('Informe a temperatura: '))

if temperatura > 90:
    print('Emergência!')
elif 60 <= cpu <= 80:
    print('Atenção')
elif 80 < cpu <= 95:
    print('Crítico')
elif cpu > 95:
    print('Emergência')