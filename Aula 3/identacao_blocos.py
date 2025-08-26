# Identar codigos em Python é uma forma de manter o código fonte mais legível e manutenível. No entando, em Python, identação tem mais uma função, o interpretador Python consegue determinar onde um bloco de código começa e onde termina de acordo com a identação do código
# Se o codigo não for identado, ele não vai funcionar 

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado")
        saldo-= valor
        print(f'Retire seu dinheiro no caixa! Novo saldo: {saldo}')
    print('Obrigado por ser nosso cliente, tenha um bom dia!')

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f'Obrigado por depositar seu dinheiro! Novo saldo: {saldo}')

# sacar(int(input('Insira o valor a ser sacado: ')))
depositar(int(input('Insira o valor a ser depositado: ')))


