def invertir_numero():
    while True:
        try:
            num = int(input("Ingrese un número de tres dígitos (100-999): "))
            if 100 <= num <= 999:
                centena = num // 100
                decena = (num // 10) % 10
                unidad = num % 10
                num_invertido = (unidad * 100) + (decena * 10) + centena
                return f"Número invertido: {num_invertido}"
            else:
                print("El número debe tener tres dígitos")
        except ValueError:
            print("Datos ingresados invalidos. Por favor, ingrese un numero entero de tres digitos.")


print(invertir_numero())

