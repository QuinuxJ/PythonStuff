def cambiarUltimoNumero(num1,num2):
    if not (100 <= num1 <= 999 and 100 <= num2 <= 999):
        return "Los números deben tener tres dígitos."
    ultimo_num1 = num1 % 10
    ultimo_num2 = num2 % 10
    nuevo_num1 = (num1 // 10) * 10 + ultimo_num2
    nuevo_num2 = (num2 // 10) * 10 + ultimo_num1
    
    return f"Numeros cambiados:\nA={nuevo_num1}\nB={nuevo_num2}"

num1 = int(input("Ingrese el primer número (100-999): "))
num2 = int(input("Ingrese el segundo número (100-999): "))

print(cambiarUltimoNumero(num1,num2))
    