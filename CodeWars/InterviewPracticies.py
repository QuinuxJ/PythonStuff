
# Tercera Parte: Caso Práctico
# Problema 1:
# Tienes un arreglo de números enteros. 
# Escribe un algoritmo en Python para encontrar 
# los tres números más grandes del arreglo, 
# pero sin usar las funciones incorporadas sort() o max().

def problema1(arr):
    threeNm = []
    for i in arr:
        num = i
        for j in arr:
            if j > num:
                num = j
                threeNm.append(num)
            else: continue
        return threeNm
        
    
print(problema1([5,7,8,11,2,1,9,7,10,23]))

# Problema 2:
# Imagina que trabajas en un sistema distribuido 
# que debe verificar si un servidor 
# está respondiendo rápidamente. 
# Si cada servidor responde con un tiempo en milisegundos, 
# escribe un programa en Python 
# que identifique qué servidores 
# están por encima de un tiempo promedio de respuesta.

def milisegundos(servidor,time):
    servidores_altos = {}
    tiempo_promedio = 500
    if time > tiempo_promedio:
        servidores_altos["Servidor con tiempo alto"] = servidor
    return servidores_altos
    
print(milisegundos("USA",300))
print(milisegundos("MX",150))
print(milisegundos("ENG",600))
print(milisegundos("CHINA",502))
print(milisegundos("RUS",499))