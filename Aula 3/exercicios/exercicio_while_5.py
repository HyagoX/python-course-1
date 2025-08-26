numero = int(input('Digite um numero: '))
primo = True

for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo and numero > 1:
    print(f'{numero} é primo')
else:
    print(f'{numero} nao é primo')