numero1 = int(input('Digite o primeiro número?'))
numero2 = int(input('Digite o segundo número?'))
opereção = input('Qual o opereção você quer fazer?')

if opereção == '+':
    resultado = numero1 + numero2
    print(f'O resultado da sua operação é: {numero1}{opereção}{numero2}={resultado}')
elif opereção == '-':
    resultado = numero1 - numero2
    print(f'O resultado da sua operação é: {numero1}{opereção}{numero2}={resultado}')
elif opereção == '*':
    resultado = numero1 * numero2
    print(f'O resultado da sua operação é: {resultado}')
elif opereção == '/':
    resultado = numero1 / numero2
    print(f'O resultado da sua operação é: {resultado}')
