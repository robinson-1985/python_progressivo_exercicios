''' 5. Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o 
valor das variáveis e exiba na tela. '''

var1 = int(input('Primeiro numero: '))
var2  = int(input('Segundo numero : '))

print('Variavel 1: ', var1)
print('Variavel 2: ', var2)
print('Invertendo...')

aux  = var2
var2 = var1
var1 = aux

print('Variavel 1: ', var1)
print('Variavel 2: ', var2)
