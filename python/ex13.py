numero = int(input("Escreve um numero para ver a tabuada: "))

contador = 1

print(f"\nTabuada de {numero}:")
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
