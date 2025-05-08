def ahorro():
    montoInicial = 0
    totalMes = 0
    montoFinalM = 0
    montoFinal = 0
    totalAnio = 0
    try:
        montoInicial = float(input("Ingresa tu monto incial: "))
        montoFinal = montoInicial
        for i in range(51):
            totalAnio = totalAnio + montoFinal
            
            if i == 3:
                totalMes = totalAnio
                montoFinalM = montoFinal
            montoFinal = montoFinal*2
    except:
        print('Introduce un valor correcto')
      
    return f"En 1 Mes ahorraste: {totalMes} pesos dando un monto incial de: {montoInicial}\nMonto Final: {montoFinalM}\nAhorro Total del año: {totalAnio:17.2f}, Monto Final: {montoFinal/2:17.2f}"


print(ahorro())