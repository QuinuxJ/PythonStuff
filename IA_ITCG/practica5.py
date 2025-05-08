def pagoTrabajador(horasT, tarifaHora, porcentajeDes):
    if horasT <= 0:
        return "Datos incorrectos"

    pagoNeto = 0
    pagoHX = 0
    horasEx = 0

    if (horasT > 40):
        horasEx = horasT - 40
        pagoNeto = 40 * tarifaHora
        tarifaExtra = tarifaHora * 1.5
        pagoHX = horasEx * tarifaExtra
    else:
        pagoNeto = horasT * tarifaHora

    pagoTotal = pagoNeto + pagoHX
    descuento = pagoTotal * (porcentajeDes / 100)
    pagoFinal = pagoTotal - descuento

    return horasT, tarifaHora, porcentajeDes, horasEx, pagoFinal

try:
    horasT = int(input("Ingresa tus horas trabajadas: "))
    tarifaHora = int(input("Ingresa la tarifa por hora: "))
    porcentajeDes = int(input("Ingresa el porcentaje de descuento: "))

    resultado = pagoTrabajador(horasT, tarifaHora, porcentajeDes)

    if resultado == "Datos incorrectos":
        print(resultado)
    else:
        horasT, tarifaHora, porcentajeDes, horasEx, pagoFinal = resultado
        print(f"\nTrabajador Datos:")
        print(f"Horas Trabajadas: {horasT}")
        print(f"Tarifa por hora: {tarifaHora}")
        print(f"Porcentaje de descuento: {porcentajeDes}%")
        print(f"Horas extras: {horasEx}")
        print(f"Total de su pago: {pagoFinal:.2f}")

except ValueError:
    print("Datos ingresados incorrectamente. Debes ingresar números enteros.")
