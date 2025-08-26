# Verifica se existe um objeto dentro de uma sequência(Lista de objetos), retornando True ou False. CASE SENSITIVE
frutas = ['limao', 'uva']
curso = 'Curso de Python'

# Verifica se um objeto está em uma sequência
print('laranja' in frutas)

# Verifica se um objeto NÃO está em uma sequência
print('limao' not in frutas)

# Também é valido em Strings
print('Python' in curso)

# Exemplo de possivel erro:
# print('python' in curso)
# >> retorna 'FALSE' por conta de ser case sensitive(P minusculo, diferente do P dentro da variável)