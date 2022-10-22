''' 10. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, 
etc.), se digitar outro valor deve aparecer valor inválido. '''

num = int(input('Digite um número correspondente ao dia da semana:  \n1-Domingo \n2-Segunda \n3-Terça \n4-Quarta \n5-Quinta \n6-Sexta \n7-Sábado \n'))

if num== 1 :
    print('Domingo')
elif num== 2 :
    print('Segunda-feira')
elif num== 3 :
    print('Terça-feira')
elif num== 4 :
    print('Quarta-feira')
elif num== 5 :
    print('Quinta-feira')
elif num== 6:
    print('Sexta-feira')
elif num== 7:
    print('Sábado')
else:
    print('Valor inválido')
