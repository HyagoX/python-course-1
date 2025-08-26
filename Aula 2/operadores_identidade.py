# Operadores de identidade verificam se duas ou mais variaveis ocupam(True) ou não ocupam(False) o mesmo espaço na memória
curso = 'Curso de Python'
nome_curso = curso
saldo, limite = 200, 200

# Valores Iguais das duas variaveis, retorna True
print(saldo is limite)

# Mesma coisa com Strings. Valores Iguais das duas variaveis, retorna True
print(curso is nome_curso)

# Utilizando operadores de comparação para verificar se NÃO ocupam o mesmo espaço na memória. Nesse caso, eles ocupam, entao retorna false
print(curso is not nome_curso)