''' 17. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade 
de centenas, dezenas e unidades do mesmo. Observando os termos no plural a colocação do 
"e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25,
20, 10, 21, 11, 1, 7 e 16. '''

numero = int(input('Digite um número menor que 1000: '))
centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10

if centena == 1:
    print(centena, 'centena,', end=' ')
elif centena > 1:
    print(centena, 'centenas,', end=' ')

if dezena == 1:
    print(dezena, 'dezena e', end=' ')  
elif dezena > 1:
    print(dezena, 'dezenas e', end=' ')
    
if unidade == 1:
    print(unidade, 'unidade')
elif unidade > 1:
    print(unidade, 'unidades')
    
if centena == 0 and dezena == 0 and unidade == 0:
    print('0')  
