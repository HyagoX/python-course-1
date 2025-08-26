# Curso de Python - Fundamentos Completos 🐍

Este repositório contém todo o material desenvolvido durante o curso de fundamentos de Python, abordando desde conceitos básicos até estruturas mais avançadas da linguagem.

---

# Aula 1: Fundamentos de Python - Aula Prática

Este repositório contém os códigos desenvolvidos durante a aula de fundamentos de Python, abordando conceitos essenciais para iniciantes na linguagem.

## 📚 Conteúdo da Aula

### 1. Variáveis e Constantes (`variaveis_constantes.py`)

**Conceitos abordados:**
- Declaração de variáveis
- Atribuição múltipla de variáveis
- Convenções para constantes em Python
- Uso de f-strings para formatação de texto

**Pontos importantes:**
- Em Python, não existe diferenciação técnica entre variáveis e constantes
- Por convenção, constantes são escritas em MAIÚSCULO
- É possível atribuir valores a múltiplas variáveis em uma única linha
- F-strings (`f"texto {variavel}"`) facilitam a interpolação de variáveis em strings

**Exemplo prático:**
```python
nome, idade = 'Hyago', 17
LIMITE_SAQUE_DIARIO = 1000  # Constante por convenção
print(f"Meu nome é {nome} e tenho {idade} anos")
```

### 2. Conversão de Tipos (`convertendo_tipos.py`)

**Conceitos abordados:**
- Verificação de tipos com `type()`
- Diferença entre divisão inteira (`//`) e divisão real (`/`)
- Conversão explícita de tipos (`int()`, `float()`)

**Pontos importantes:**
- A divisão com `/` sempre retorna um float
- A divisão com `//` retorna um int (divisão inteira)
- Python permite conversão entre tipos numéricos quando compatível
- A função `type()` é útil para verificar o tipo de uma variável

**Exemplo prático:**
```python
preco = 10
divisao_real = preco / 2    # Resultado: 5.0 (float)
divisao_inteira = preco // 3  # Resultado: 3 (int)
```

### 3. Entrada e Saída de Dados (`print_input.py`)

**Conceitos abordados:**
- Captura de entrada do usuário com `input()`
- Formatação de saída com `print()`
- Parâmetros `sep` e `end` da função `print()`

**Pontos importantes:**
- `input()` sempre retorna uma string
- O parâmetro `sep` define o separador entre valores no print
- O parâmetro `end` define o que será impresso ao final (padrão é `\n`)
- Duas formas principais de formatação: f-strings e parâmetros do print

**Exemplo prático:**
```python
nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')
print(nome, idade, sep=' - ', end='!\n')
```

## 🎯 Objetivos de Aprendizado

Após estudar estes códigos, você deve ser capaz de:

1. **Trabalhar com variáveis**: Criar, modificar e usar variáveis em Python
2. **Entender tipos de dados**: Reconhecer diferentes tipos e fazer conversões
3. **Interagir com o usuário**: Capturar entrada e exibir saída formatada
4. **Aplicar boas práticas**: Usar convenções adequadas para nomes e constantes

---

# Aula 2: Operadores em Python 🐍

## 📋 Conteúdo da Aula

Esta aula abordou os diferentes tipos de operadores disponíveis em Python, fundamentais para manipular dados e criar lógica em nossos programas.

## 📚 Operadores Estudados

### 1. Operadores Aritméticos (`operadores_aritmeticos.py`)

Os operadores básicos para realizar cálculos matemáticos:

- **Adição (`+`)**: Soma dois valores
- **Subtração (`-`)**: Subtrai o segundo valor do primeiro
- **Multiplicação (`*`)**: Multiplica dois valores
- **Divisão (`/`)**: Divide e retorna um **FLOAT**
- **Divisão Inteira (`//`)**: Divide e retorna apenas a parte inteira (**INT**)
- **Módulo (`%`)**: Retorna o resto da divisão
- **Exponenciação (`**`)**: Eleva um número a uma potência

```python
print(10 + 2)    # 12
print(10 / 2)    # 5.0 (float)
print(10 // 2)   # 5 (int)
print(10 % 3)    # 1 (resto da divisão)
print(10 ** 3)   # 1000 (10³)
```

### 2. Operadores de Associação (`operadores_associacao.py`)

Verificam se um objeto existe dentro de uma sequência:

- **`in`**: Verifica se existe
- **`not in`**: Verifica se NÃO existe

⚠️ **Importante**: São **case sensitive** (diferencia maiúsculas de minúsculas)

```python
frutas = ['limao', 'uva']
curso = 'Curso de Python'

print('limao' in frutas)     # True
print('laranja' in frutas)   # False
print('Python' in curso)    # True
print('python' in curso)    # False (case sensitive!)
```

### 3. Operadores de Atribuição (`operadores_atribuicao.py`)

Permitem atribuir e modificar valores de variáveis:

- **`=`**: Atribuição simples
- **`+=`**: Adição e atribuição
- **`-=`**: Subtração e atribuição
- **`*=`**: Multiplicação e atribuição
- **`/=`**: Divisão e atribuição
- **`//=`**: Divisão inteira e atribuição
- **`%=`**: Módulo e atribuição
- **`**=`**: Exponenciação e atribuição

```python
saldo = 500
saldo += 200  # saldo = saldo + 200
saldo *= 2    # saldo = saldo * 2
```

### 4. Operadores de Comparação (`operadores_comparacao.py`)

Comparam valores e retornam `True` ou `False`:

- **`==`**: Igualdade
- **`!=`**: Diferença
- **`>`**: Maior que
- **`>=`**: Maior ou igual
- **`<`**: Menor que
- **`<=`**: Menor ou igual

```python
saldo = 200
saque = 200

print(saldo == saque)  # True
print(saldo > saque)   # False
print(saldo >= saque)  # True
```

### 5. Operadores de Identidade (`operadores_identidade.py`)

Verificam se duas variáveis ocupam o mesmo espaço na memória:

- **`is`**: Verifica se ocupam o mesmo espaço
- **`is not`**: Verifica se NÃO ocupam o mesmo espaço

```python
curso = 'Curso de Python'
nome_curso = curso

print(curso is nome_curso)      # True
print(curso is not nome_curso)  # False
```

### 6. Operadores Lógicos (`operadores_logicos.py`)

Combinam expressões lógicas:

- **`and`**: Retorna `True` apenas se ambas as condições forem verdadeiras
- **`or`**: Retorna `True` se pelo menos uma condição for verdadeira
- **`not`**: Inverte o valor lógico

```python
saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Usando and
resultado = saldo >= saque and saque <= limite

# Usando or
resultado = saldo >= saque or conta_especial

# Combinando com parênteses para clareza
resultado = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
```

### 7. Precedência de Operadores (`precedencia.py`)

Python segue as regras matemáticas de precedência:

1. **Parênteses** `()`
2. **Exponenciação** `**`
3. **Multiplicação e Divisão** `*`, `/`, `//`, `%` (da esquerda para direita)
4. **Adição e Subtração** `+`, `-` (da esquerda para direita)

```python
print(10 - 5 * 2)      # 0 (não 10)
print((10 - 5) * 2)    # 10
print(10 ** 2 * 2)     # 200 (100 * 2)
print(10 / 2 * 4)      # 20.0 (5.0 * 4)
```

## 🎯 Conceitos Principais Aprendidos

- **Diferença entre `/` e `//`**: Divisão comum vs divisão inteira
- **Case Sensitivity**: Python diferencia maiúsculas de minúsculas
- **Precedência**: A ordem correta de execução das operações
- **Operadores de Identidade vs Igualdade**: `is` verifica memória, `==` verifica valor
- **Combinação de Operadores Lógicos**: Uso de parênteses para clareza

---

# Aula 3: Estruturas de Controle em Python 🐍

## 📋 Conteúdo da Aula

Esta aula abordou as estruturas de controle que permitem alterar o fluxo de execução do programa, incluindo estruturas condicionais, laços de repetição e a importância da identação em Python.

## 📚 Conceitos Estudados

### 1. Estruturas Condicionais (`estruturas_condicionais.py`)

As estruturas condicionais permitem o **desvio de fluxo de controle** quando determinadas expressões lógicas são atendidas.

#### If/Elif/Else

Estrutura básica para tomada de decisões:

```python
MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH')
elif idade >= IDADE_ESPECIAL:
    print('Pode fazer as aulas teóricas, mas não as aulas práticas')
else:
    print('Ainda não pode tirar a CNH')
```

#### If Aninhado

Estruturas condicionais dentro de outras estruturas condicionais:

```python
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
        print('Não foi possível realizar o saque, saldo insuficiente!')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')
```

#### If Ternário

Forma concisa de escrever uma condição simples:

```python
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
```

### 2. Identação e Blocos de Código (`identacao_blocos.py`)

Em Python, a **identação** não é apenas para legibilidade - é **obrigatória** e define onde um bloco de código começa e termina.

⚠️ **Importante**: Se o código não for identado corretamente, ele não funcionará!

```python
def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("Valor sacado")
        saldo -= valor
        print(f'Retire seu dinheiro no caixa! Novo saldo: {saldo}')
    print('Obrigado por ser nosso cliente, tenha um bom dia!')

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f'Obrigado por depositar seu dinheiro! Novo saldo: {saldo}')
```

### 3. Laços de Repetição (`lacos_repeticao.py`)

Estruturas que permitem executar um bloco de código repetidamente.

#### Laço FOR

Itera sobre elementos de uma sequência (iterável):

```python
texto = input('Insira o seu texto: ')
VOGAIS = 'AEIOU'

# Iterando sobre caracteres de uma string
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
else:
    print()
    print('Executa no final do laço')
```

#### FOR com Range

Usando a função `range()` para criar sequências numéricas:

```python
# Imprime a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=' ''\n')
```

**Sintaxe do range():**
- `range(stop)`: de 0 até stop-1
- `range(start, stop)`: de start até stop-1
- `range(start, stop, step)`: de start até stop-1, com incremento step

#### Laço WHILE

Executa enquanto uma condição for verdadeira:

```python
opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n'))
    
    if opcao == 1:
        print("Realizando Saque")
        break
    elif opcao == 2:
        print("Exibindo extrato...")
        break
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")
```

## 🎯 Conceitos Principais Aprendidos

### Estruturas Condicionais
- **if/elif/else**: Tomada de decisões baseada em condições
- **If aninhado**: Condições dentro de outras condições
- **If ternário**: Forma concisa para condições simples

### Controle de Fluxo
- **break**: Interrompe o laço completamente
- **continue**: Pula para a próxima iteração
- **else em laços**: Executa quando o laço termina normalmente (sem break)

### Laços de Repetição
- **for**: Ideal para iterar sobre sequências conhecidas
- **while**: Ideal para repetições baseadas em condições
- **range()**: Gera sequências numéricas para usar com for

### Identação
- **Obrigatória** em Python
- Define blocos de código
- Melhora a legibilidade e manutenibilidade

---

# Aula 4: Manipulação de Strings em Python 🐍

## 📋 Conteúdo da Aula

Esta aula focou na manipulação de strings em Python, abordando técnicas de fatiamento, interpolação, formatação e métodos úteis para trabalhar com texto.

## 📚 Conceitos Estudados

### 1. Fatiamento de Strings (`fatiamento_string.py`)

O fatiamento permite extrair **substrings** (partes) de uma string original usando índices.

**Sintaxe**: `string[início:fim:passo]`

```python
nome = 'Hyago Jose Maria'

print(nome[0])        # 'H' - primeiro caractere
print(nome[:5])       # 'Hyago' - do início até índice 4
print(nome[6:10])     # 'Jose' - do índice 6 ao 9
print(nome[6:10:2])   # 'Js' - do índice 6 ao 9, pulando de 2 em 2
print(nome[:])        # 'Hyago Jose Maria' - string completa
print(nome[::-1])     # 'airaM esoJ ogayH' - string invertida
```

**Regras importantes:**
- Índices negativos contam do final para o início
- `[::-1]` inverte completamente a string
- Omitir início/fim usa o começo/final da string
- Passo negativo inverte a direção

### 2. Interpolação de Strings (`interpolacao_strings.py`)

Diferentes formas de inserir variáveis dentro de strings.

#### Método Old Style (%)

```python
nome = 'Hyago'
idade = 17
profissao = 'Programador' 
linguagem = 'Python'

print('Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s' % (nome, idade, profissao, linguagem))
```

**Especificadores comuns:**
- `%s` - String
- `%d` - Inteiro
- `%f` - Float

#### Método format()

```python
# Posicional
print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem))

# Com índices específicos
print('Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}'.format(linguagem, profissao, idade, nome))
```

#### F-Strings (Recomendado) ⭐

Forma mais moderna e legível:

```python
print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.')

# Formatação numérica
PI = 3.14159
print(f'Valor de PI: {PI:.2f}')      # 3.14 (2 casas decimais)
print(f'Valor de PI: {PI:10.2f}')    # '      3.14' (10 caracteres, 2 decimais)
```

### 3. Métodos de Strings - Parte 1 (`strings_1.py`)

#### Transformação de Caso

```python
nome = 'Hyago'

print(nome.upper())    # 'HYAGO' - maiúsculas
print(nome.lower())    # 'hyago' - minúsculas  
print(nome.title())    # 'Hyago' - primeira letra maiúscula
```

#### Remoção de Espaços

```python
texto = '  Olá Mundo    '

print(texto.strip())   # 'Olá Mundo' - remove espaços do início e fim
print(texto.lstrip())  # 'Olá Mundo    ' - remove espaços da esquerda
print(texto.rstrip())  # '  Olá Mundo' - remove espaços da direita
```

#### Centralização e Junção

```python
menu = 'Python'

print('###' + menu + '###')     # '###Python###'
print(menu.center(12,'#'))      # '###Python###' - centraliza com 12 caracteres
print('-'.join(menu))           # 'P-y-t-h-o-n' - junta caracteres com '-'
```

### 4. Strings Multilinhas (`strings_multilinhas.py`)

Strings que ocupam múltiplas linhas usando aspas triplas (`'''` ou `"""`):

```python
nome = 'Hyago'

mensagem = f''' 
    Olá meu nome é {nome} 
Estou aprendendo Python
    Essa mensagem tem diferentes recuos
'''
print(mensagem)

# Exemplo prático - Menu
print('''
 ========== MENU ===========
    
    1 - Depositar
    2 - Sacar
    3 - Sair
      
 ============================
      Obrigado por usar o nosso sistema!!!
''')
```

**Vantagens das strings multilinhas:**
- Preservam quebras de linha
- Mantêm formatação e recuos
- Ideais para menus, templates, documentação
- Suportam interpolação com f-strings

## 🎯 Conceitos Principais Aprendidos

### Fatiamento
- **Índices positivos e negativos**
- **Sintaxe [início:fim:passo]**
- **Inversão de strings com [::-1]**

### Interpolação
- **Old Style (%)**: Método clássico
- **format()**: Método intermediário com mais flexibilidade
- **F-Strings**: Método moderno, mais legível e eficiente

### Métodos Úteis
- **Transformação**: `upper()`, `lower()`, `title()`
- **Limpeza**: `strip()`, `lstrip()`, `rstrip()`
- **Formatação**: `center()`, `join()`

### Strings Multilinhas
- **Aspas triplas** para textos longos
- **Preservação de formatação**
- **Combinação com f-strings**

## 📊 Tabela de Métodos de String

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `upper()` | Converte para maiúsculas | `'python'.upper()` → `'PYTHON'` |
| `lower()` | Converte para minúsculas | `'PYTHON'.lower()` → `'python'` |
| `title()` | Primeira letra maiúscula | `'python'.title()` → `'Python'` |
| `strip()` | Remove espaços das extremidades | `' python '.strip()` → `'python'` |
| `center(n, char)` | Centraliza com n caracteres | `'py'.center(6, '-')` → `'--py--'` |
| `join(iterável)` | Une elementos com separador | `'-'.join('abc')` → `'a-b-c'` |

## 🔧 Formatação de Números em F-Strings

| Formato | Descrição | Exemplo |
|---------|-----------|---------|
| `{var:.2f}` | 2 casas decimais | `{3.14159:.2f}` → `3.14` |
| `{var:10.2f}` | 10 chars, 2 decimais | `{3.14:.2f}` → `'      3.14'` |
| `{var:>10}` | Alinha à direita | `{'py':>10}` → `'        py'` |
| `{var:<10}` | Alinha à esquerda | `{'py':<10}` → `'py        '` |

---

# Aula 5: Funções em Python 🐍

## 📋 Conteúdo da Aula

Esta aula abordou conceitos fundamentais sobre funções em Python, incluindo definição, parâmetros, argumentos, escopo de variáveis e conceitos avançados como funções de primeira classe.

## 📚 Conceitos Estudados

### 1. Definindo Funções (`funcoes.py`)

Fundamentos sobre criação e uso de funções em Python.

#### Funções Básicas

```python
def exibir_mensagem():
    print('Ola mundo!')

def exibir_mensagem2(nome):
    print(f'Seja bem vindo {nome}!')

def exibir_mensagem3(nome='Anonimo'):
    print(f'Seja bem vindo {nome}!')
```

#### Funções com Retorno

```python
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor  # Retorna uma tupla
```

**Pontos importantes:**
- Funções sem `return` retornam `None` por padrão
- Uma função pode retornar múltiplos valores (tupla)
- Parâmetros podem ter valores padrão

### 2. Parâmetros Somente por Posição (`parametros_por_posicao.py`)

Uso do separador `/` para forçar parâmetros posicionais.

```python
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Válido
criar_carro('Palio', 1999, 'ABC-1234', 'Fiat', '1.0', combustivel='Gasolina')

# Inválido - não pode passar por nome os primeiros parâmetros
# criar_carro(modelo='Palio', ano=1999, placa='ABC-1234', ...)
```

**Estrutura:**
```
def funcao(pos_only, /, pos_or_keyword, keyword_only):
           |          |                 |
           |          |                 └── Somente por nome
           |          └── Por posição ou nome
           └── Somente por posição
```

### 3. Parâmetros Somente por Nome (`parametros_por_nome.py`)

Uso do separador `*` para forçar parâmetros nomeados.

```python
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Válido - todos os parâmetros devem ser nomeados
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", 
           marca="Fiat", motor="1.0", combustivel="Gasolina")

# Inválido - não pode passar por posição
# criar_carro("Palio", 1999, "ABC-1234", ...)
```

### 4. Parâmetros Mistos (`parametros_mistos.py`)

Combinação de parâmetros posicionais e nomeados.

```python
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Válido
criar_carro("Palio", 1999, "ABC-1234", 
           marca="Fiat", motor="1.0", combustivel="Gasolina")
```

**Estrutura completa:**
- `modelo, ano, placa`: Somente por posição (antes de `/`)
- `marca, motor, combustivel`: Somente por nome (depois de `*`)

### 5. Argumentos Nomeados (`argumentos_nomeados.py`)

Diferentes formas de passar argumentos para funções.

```python
def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso: {marca}/{modelo}/{ano}/{placa}')

# Forma tradicional
salvar_carro('Fiat', 'Palio', 1999, 'ABC-1234')

# Por nome
salvar_carro(marca='Fiat', modelo='Palio', ano=1999, placa='ABC-1234')

# Usando dicionário com **
salvar_carro(**{'marca':'Fiat', 'modelo':'Palio', 'ano':1999, 'placa':'ABC-1234'})
```

### 6. *args e **kwargs (`args_kwargs.py`)

Função que aceita quantidade variável de argumentos.

```python
def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema(
    'Sexta-Feira, 24 de Agosto de 2025',
    'Zen of Python',
    'Beautiful is better than ugly.',
    'Explicit is better than implicit.',
    autor="Tim Peters",
    ano=1999
)
```

**Conceitos:**
- **`*args`**: Recebe argumentos posicionais extras como tupla
- **`**kwargs`**: Recebe argumentos nomeados extras como dicionário
- Permite funções com número variável de parâmetros

### 7. Escopo Local e Global (`escopo_local_e_global.py`)

Entendendo o escopo de variáveis em funções.

```python
salario = 2000  # Variável global

def salario_bonus(bonus):
    global salario
    lista_aux = lista.copy()  # Variável local
    lista_aux.append(2)
    print(f'Lista Auxiliar={lista_aux}')
    salario += bonus  # Modifica a variável global
    return salario

lista = [1]  # Variável global
novo_salario = salario_bonus(500)
print(novo_salario)  # 2500
```

**Conceitos importantes:**
- **Escopo Local**: Variáveis criadas dentro da função
- **Escopo Global**: Variáveis criadas fora da função
- **`global`**: Palavra-chave para modificar variáveis globais dentro da função
- **`.copy()`**: Cria uma cópia para evitar modificar a original

### 8. Funções de Primeira Classe (`objetos_primeira_classe.py`)

Em Python, funções são objetos de primeira classe.

```python
def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação {a} + {b} = {resultado}')

# Passando funções como argumentos
exibir_resultado(10, 10, somar)      # 20
exibir_resultado(10, 10, multiplicar) # 100

# Atribuindo função a uma variável
op = somar
print(op(1, 50))  # 51
```

**Características de primeira classe:**
- Podem ser armazenadas em variáveis
- Podem ser passadas como argumentos
- Podem ser retornadas por outras funções
- Podem ser armazenadas em estruturas de dados

## 🎯 Conceitos Principais Aprendidos

### Definição de Funções
- **Sintaxe básica**: `def nome_funcao():`
- **Parâmetros opcionais** com valores padrão
- **Múltiplos retornos** usando tuplas

### Tipos de Parâmetros
- **Posicionais**: Antes de `/`
- **Posicionais ou Nomeados**: Entre `/` e `*`
- **Somente Nomeados**: Depois de `*`

### Argumentos Variáveis
- **`*args`**: Argumentos posicionais extras (tupla)
- **`**kwargs`**: Argumentos nomeados extras (dicionário)

### Escopo de Variáveis
- **Local**: Dentro da função
- **Global**: Fora da função
- **`global`**: Modificar variáveis globais

### Funções de Primeira Classe
- **Flexibilidade**: Funções como valores
- **Programação funcional**: Passar funções como argumentos
- **Reutilização**: Maior modularidade do código

## 📊 Tabela de Sintaxe de Parâmetros

| Sintaxe | Tipo | Exemplo | Chamada |
|---------|------|---------|---------|
| `def f(a, b):` | Posicional ou nomeado | `f(1, 2)` ou `f(a=1, b=2)` |
| `def f(a, b, /):` | Somente posicional | `f(1, 2)` ✅ `f(a=1, b=2)` ❌ |
| `def f(*, a, b):` | Somente nomeado | `f(a=1, b=2)` ✅ `f(1, 2)` ❌ |
| `def f(a, /, b, *, c):` | Misto | `f(1, b=2, c=3)` |
| `def f(*args):` | Args variáveis | `f(1, 2, 3, 4)` |
| `def f(**kwargs):` | Kwargs variáveis | `f(a=1, b=2)` |

---

## 📁 Estrutura do Projeto

```
Python/
├── Aula 1/                  # Fundamentos básicos
│   ├── convertendo_tipos.py
│   ├── exercicios.py
│   ├── print_input.py
│   └── variaveis_constantes.py
├── Aula 2/                  # Operadores
│   ├── operadores_aritmeticos.py
│   ├── operadores_associacao.py
│   ├── operadores_atribuicao.py
│   ├── operadores_comparacao.py
│   ├── operadores_identidade.py
│   ├── operadores_logicos.py
│   └── precedencia.py
├── Aula 3/                  # Estruturas de controle
│   ├── estruturas_condicionais.py
│   ├── identacao_blocos.py
│   ├── lacos_repeticao.py
│   └── exercicios/
│       ├── exercicio_for_*.py
│       └── exercicio_while_*.py
├── Aula 4/                  # Manipulação de strings
│   ├── fatiamento_string.py
│   ├── interpolacao_strings.py
│   ├── string_1.py
│   └── strings_multilinhas.py
├── Aula 5/                  # Funções
│   ├── funcoes.py
│   ├── parametros_por_posicao.py
│   ├── parametros_por_nome.py
│   ├── parametros_mistos.py
│   ├── argumentos_nomeados.py
│   ├── args_kwargs.py
│   ├── escopo_local_e_global.py
│   ├── objetos_primeira_classe.py
│   └── exercicio/
│       └── ex_args_kwargs.py
└── Projeto/                 # Projeto prático
    └── sistema_bancario.py
```

## 🎯 Progressão do Aprendizado

### Nível Iniciante (Aulas 1-2)
- ✅ Variáveis e tipos de dados
- ✅ Entrada e saída de dados
- ✅ Operadores matemáticos e lógicos
- ✅ Conversão de tipos

### Nível Intermediário (Aulas 3-4)
- ✅ Estruturas condicionais
- ✅ Laços de repetição
- ✅ Manipulação de strings
- ✅ Controle de fluxo

### Nível Avançado (Aula 5)
- ✅ Definição de funções
- ✅ Parâmetros e argumentos
- ✅ Escopo de variáveis
- ✅ Funções de primeira classe

## 💡 Próximos Passos

Após dominar esses conceitos fundamentais, você estarei pronto para:

1. **Estruturas de Dados**: Listas, tuplas, dicionários e conjuntos
2. **Orientação a Objetos**: Classes, objetos, herança e polimorfismo
3. **Manipulação de Arquivos**: Leitura e escrita de arquivos
4. **Tratamento de Exceções**: Try/except e debugging
5. **Módulos e Pacotes**: Organização e reutilização de código
6. **Bibliotecas Externas**: pandas, numpy, requests, etc.

## 🚀 Projeto Prático

O projeto do **Sistema Bancário** (`Projeto/sistema_bancario.py`) consolida todos os conceitos aprendidos:

- Variáveis e constantes
- Estruturas condicionais
- Laços de repetição
- Funções customizadas
- Manipulação de strings
- Controle de fluxo

---

*Desenvolvido durante o curso de Python - Do básico ao avançado. Este material serve como referência completa para os fundamentos da linguagem Python.* 🐍

## 📞 Suporte

Se você tiver dúvidas sobre qualquer conceito, consulte os arquivos de código correspondentes em cada aula. Cada exemplo foi cuidadosamente desenvolvido para demonstrar os conceitos de forma prática e aplicável.

**Happy Coding!** 🎉
