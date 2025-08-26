# Definindo funções em python

def exibir_mensagem():
    print('Ola mundo!')

def exibir_mensagem2(nome):
    print(f'Seja bem vindo {nome}!')

def exibir_mensagem3(nome='Anonimo'):
    print(f'Seja bem vindo {nome}!')

# exibir_mensagem()
# exibir_mensagem2('Hyago')
# exibir_mensagem3('Hyago')

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
# retorna uma tupla, pois o valor é imutável
    return antecessor, sucessor

def func_3():
    print('Ola mundo!')


print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
print(func_3()) # None

