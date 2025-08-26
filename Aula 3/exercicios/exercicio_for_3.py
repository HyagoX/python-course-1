# Crie um programa que imprima a tabuada de um número qualquer. O numero pode ser digitado pelo usuário

numero = int(input('Digite um numero: '))

for numero in range(0, 101, numero):
    print(numero, end=' ')