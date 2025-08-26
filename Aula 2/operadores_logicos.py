print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(True and True)

# And (E)
saldo >= saque and saque <= limite

# Or (Ou)
saldo >= saque or saque <= limite

# Podemos utilizar o conceito da precendencia com os parenteses junto de outros tipos de operadores
ex = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(ex)

ex_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(ex_2)

