# Verifica se o numero inserido é par ou impar e então se o número for impar, o loop é encerrado e o número aparece no console

for numero in range(0, 21):
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')
