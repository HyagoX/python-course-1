# Crie um programa que calcule o fatorial de um número. O número deve ser informado pelo usuário e o resultado deve ser impresso.

num = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
contador = num

while contador > 1:
    fatorial *= contador
    contador -= 1

print(f"O fatorial de {num} é {fatorial}")