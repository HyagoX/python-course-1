# Variaveis para nome e idade
nome = "Hyago"
idade = 17

# Também é possivel definir ou alterar os dados de duas ou mais variaveis(como está sendo feito na linha abaixo) em uma só linha 
nome, idade = 'Natan', 23

print(f"Meu nome é {nome} e tenho {idade} anos de idade")

limite_saque_diario = 1000

# constantes sao definidas com todas as letras em maiusculo por convenção, pois a linguagem Python nao sabe diferenciar uma variavel de uma constante
ESTADOS = [
    'SP',
    'RJ',
    'SC',
    'RS'
]

nome, idade, estado = 'Hyago', 17, 'PR'
print(estado)