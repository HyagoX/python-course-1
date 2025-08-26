menu = '''
=============================

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair


'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor_deposito):
    global saldo
    global numero_saques
    global limite
    if valor_deposito >= 0 and valor_deposito <= 500:
        saldo_final = saldo + valor_deposito
        print(f'Valor depositado: {valor_deposito}, voce tem atualmente {saldo_final} de saldo')
        global extrato
        extrato += f'Deposito realizado: {saldo} + {valor_deposito} = {saldo_final} \n'
        saldo = saldo_final
    else:
        print('Valor para deposito muito alto ou insuficiente')


def sacar(valor_saque):
    global saldo
    global numero_saques
    global limite
    global extrato
    if numero_saques < 3 and valor_saque <= saldo and valor_saque <= limite:
        saldo_final = saldo - valor_saque
        print(f'Valor sacado, seu saldo atual é: {saldo_final}')
        extrato += f'Saque realizado: {saldo} - {valor_saque} = {saldo_final} \n'
        numero_saques = numero_saques + 1
        saldo = saldo_final
    else:
        print('Limite de saques diarios atingido...')

        


while True:
    opcao = input(menu)

    if opcao == '1':
        depositar(float(input('Digite o valor a ser depositado. Valor maximo para deposito é 500 reais: ')))

    elif opcao == '2':
        sacar(float(input('Digite o valor a ser sacado...: ')))

    elif opcao == '3':
        print(extrato)
    
    elif opcao == '4':
        print('Saindo...')
        break

    else:
        print('Operação invalida, por favor selecione novamente a operação desejada')
