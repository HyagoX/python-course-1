# Crie um programa que peça para o usuario digitar numeros e va somando. O loop deve continuar ate que a soma dos numeros atinja ou ultrapasse 1000

num = int(input('Insira o primeiro numero: '))

while num < 1000:
    numero = int(input('Insira outro numero: '))
    num = num + numero
    print(num)