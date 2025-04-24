num = int(input("Escreve um numero entre 1 e 100: "))

while num < 1 or num > 100:
    print("Numero inválido. Tente novamente.")
    num = int(input("Escreve um número entre 1 e 100: "))

print(f"O numero {num} está dentro do intervalo!")
