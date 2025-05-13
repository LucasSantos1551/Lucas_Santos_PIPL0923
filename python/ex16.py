cont = 0
soma = 0

while cont < 30:
    try:
        num = int(input(f"Digite o {cont+1}º número par entre 1 e 50: "))
        if 1 <= num <= 50 and num % 2 == 0:
            soma += num
            cont += 1
        else:
            print("Número inválido. Deve ser PAR e entre 1 e 50.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

media = soma / 30
print(f"Média dos 30 números pares: {media}")