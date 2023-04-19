''' 
22. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool: até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro

    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
    o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor 
    a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool 
    é R$ 1,90.
'''

alcool = 1.90
gasolina = 2.50

litros = float(input('Digite a quantidade de litros: '))
tipo = input('Digite o tipo de combustível (A-álcool, G-gasolina): ')

if tipo == 'A':
    if litros <= 20:
        print(f'Valor a ser pago: R$ {litros * alcool * 0.97:.2f}')
    else:
        print(f'Valor a ser pago: R$ {litros * alcool * 0.95:.2f}')
elif tipo == 'G':
    if litros <= 20:
        print(f'Valor a ser pago: R$ {litros * gasolina * 0.96:.2f}')
    else:
        print(f'Valor a ser pago: R$ {litros * gasolina * 0.94:.2f}')
else:
    print('Opção inválida')
