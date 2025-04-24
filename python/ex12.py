numero = int(input("Escreve um numero inteiro maior que 1: "))

total_operacoes = 0

print("\nResultados:")

for contador in range(1, numero):
    print(f"{numero} + {contador} = {numero + contador}")
    total_operacoes += 1

    print(f"{numero} - {contador} = {numero - contador}")
    total_operacoes += 1

    print(f"{numero} * {contador} = {numero * contador}")
    total_operacoes += 1

    if contador != 0:
        print(f"{numero} / {contador} = {numero / contador}")
        total_operacoes += 1

print(f"\nRealizou {total_operacoes} operações")
