for codigo in range(0, 256, 20):
    for i in range(codigo, codigo + 20):
        if i <= 255:
            print(f"Código {i}: {chr(i)}")
    continuar = input("\nDeseja continuar?").strip().lower()
    
    if continuar != 's':
        print("Saindo do programa...")
        break