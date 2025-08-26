def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação {a} + {b} = {resultado}\n')

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, multiplicar)

op = somar

print(op(1, 50)) # 51