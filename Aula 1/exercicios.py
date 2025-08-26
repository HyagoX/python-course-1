# Um programa que pede nome, idade e cidade, e exiba uma mensagem personalizada
# print("Exercício número um: \n", end='')
# nome = input('Informe seu nome: ')
# idade = input('Informe sua idade: ')
# cidade = input('Informe o nome da sua cidade: ')

# print(f'Olá {nome}, com {idade} anos, morando na cidade de {cidade}! Seja bem vindo!')

# Uma calculadora simples que aceite dois números e mostre diferentes tipos de divisão

print('Exercício número dois: \n')
numero_1 = int(input('Digite o primeiro Numero: '))
numero_2 = int(input('Digite o segundo Numero: '))
# print(type(numero_1 / numero_2), ' Numeros Divididos')
# -------------^ Retorna o valor da divisão em float
print(type(numero_1 // numero_2), ' Numeros Divididos')
# ---------------^ retorna os números em int no terminal.