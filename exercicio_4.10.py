print('Bem vindo ao programaa que calcula sua energia elétrica.')
consumoEnergia = float(input('Qual a quantidade consumida em kWh? '))
tipoInstalacao = input('Qual o tipo de instalação? Residencia: R, Industria: I, Comercio: C: ')
valorConsumido = 0
base = consumoEnergia
if tipoInstalacao == 'R':
    if base > 500:
        valorConsumido = (base - 500) * 0.65
        base = 500
    if base <= 500:
        valorConsumido = valorConsumido + ( base * 0.4)

if tipoInstalacao == 'I':
    if base > 1000:
        valorConsumido = valorConsumido + ((base - 1000) * 0.60)
        base = 1000
    if base <= 1000:
        valorConsumido = valorConsumido + (base * 0.55)

if tipoInstalacao == 'C':
    if base > 5000:
        valorConsumido = valorConsumido + ((base - 5000) * 0.60)
        base = 5000
    if base <= 5000:
        valorConsumido = valorConsumido + (base * 0.55)

print(f'Seu consumo de energia foi de: {consumoEnergia}, o valor da sua conta é: R${valorConsumido}')