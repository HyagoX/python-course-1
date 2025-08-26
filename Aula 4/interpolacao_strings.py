# Interpolação com o método old style %

nome = 'Hyago'
idade = 17
profissao = 'Programador'
linguagem = 'Python'

print('Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s' % (nome, idade, profissao, linguagem))

# Interpolação com o método format

print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem))
print('Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}'.format(linguagem, profissao, idade, nome))

# Interpolação com F-Strings

print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.')

PI = 3.14159

print(f'Valor de PI: {PI:.2f}')

print(f'Valor de PI: {PI:10.2f}')