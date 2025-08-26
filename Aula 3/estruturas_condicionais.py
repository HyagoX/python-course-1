# Estruturas condicionais permitem o desvio de fluxo de controle quando determinadas expressões lógicas são atendidadas

# If/Elif/Else

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH')
elif idade >= IDADE_ESPECIAL:
    print('Pode fazer as aulas teoricas, mas não as aulas práticas')
else:
    print('Ainda nao pode tirar a CNH')


# If aninhado

conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso do cheque especial')
    else:
        print('Nao foi possivel realizar o saquem saldo insuficiente!')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')


# If Ternário
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")