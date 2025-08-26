# Crie um jogo de adivinhação onde o computador escolhe um número entre 1 e 20 e o usuário tem que adivinhar. O loop deve continuar até o usuário acertar o número.
import random

numero = int(input("Digite um numero de 1 a 20: "))
computador = random.randint(0, 20)

while numero != computador:
    print('Numero errado, tente novamente')
    numero = int(input('Digite outro numero: '))