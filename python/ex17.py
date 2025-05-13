print("Múltiplos de 5 mas não de 3 (1 a 1000):")
for num in range(1, 1001):
    if num % 5 == 0 and num % 3 != 0:
        print(num, end=" ")
