
# Laço de repetição FOR
texto = input('Insira o seu texto: ')
VOGAIS = 'AEIOU'

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')

else:
    print()
    print('Executa no final do laço')

# Laço de repetição FOR com a função built-in RANGE
# Imprime a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=' ''\n')


# Laço de repetição WHILE e WHILE/ELSE
opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n'))

    if opcao == 1:
        print("Realizando Saque")
        break
    elif opcao == 2:
        print("Exibindo extrato...")
        break
else:
    print("Obrigado por usar nosso sistema bancário, até logo!") 