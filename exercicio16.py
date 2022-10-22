''' 16. Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize 
o operador módulo (resto da divisão): %'''

num = int(input('Digite um número: '))

if num % 2 == 0:
    print('Número par!')
else:
    print('Número ímpar!')
