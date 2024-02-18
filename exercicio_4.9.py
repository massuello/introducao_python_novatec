valor_casa = float(input('Qual o valor da casa?'))
valor_salario = float(input('Qual o valor do seu salário?'))
quantidade_anos = int(input('Quantos anos a pagar?'))
valor_pretacao = valor_casa / (quantidade_anos * 12)

if valor_pretacao > (valor_salario * 0.3):
    print('Reprovado o empréstimo!')
elif valor_pretacao < (valor_salario * 0.3):
    print(f'Empréstimo aprovado, valor da prestação R${valor_pretacao:6.2}')
