a, b = 1, 1
print("Série de Bonatchi (60 primeiros números):")
print(a, b, end=" ")

for _ in range(58):  # já mostramos 2
    a, b = b, a + b
    print(b, end=" ")
