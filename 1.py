import random
import time

def generar_numeros_aleatorios(minimo, maximo):
    return random.randint(minimo, maximo)
    
def operacion_numeros(operacion, tiempo_limite):
    start_time = time.time()
    print(f"Iniciando operación de {operacion} durante {tiempo_limite} segundos.")
    while time.time() - start_time < tiempo_limite:
        numero1 = generar_numeros_aleatorios(1, 100)
        numero2 = generar_numeros_aleatorios(1, 100)
        resultado = None  
        if operacion == "resta":
            resultado = numero1 - numero2
        elif operacion == "suma":
            resultado = numero1 + numero2
        elif operacion == "multiplicacion":
            resultado = numero1 * numero2
        elif operacion == "division":
            resultado = numero1 / numero2
        print(f"Números utilizados para {operacion}: {numero1} y {numero2}")
        # Verificar si resultado no es None antes de imprimir
        if resultado is not None:
            print(f"Resultado de {operacion}: {resultado}")
            
min_tiempo = 5 
max_tiempo = 15 

operacion_numeros("resta", random.uniform(min_tiempo, max_tiempo))
operacion_numeros("suma", random.uniform(min_tiempo, max_tiempo))
operacion_numeros("division", random.uniform(min_tiempo, max_tiempo))
operacion_numeros("multiplicacion", random.uniform(min_tiempo, max_tiempo))
operacion_numeros("divisom", random.uniform(min_tiempo, max_tiempo))
operacion_numeros("suma", random.uniform(min_tiempo, max_tiempo))
operacion_numeros("resta", random.uniform(min_tiempo, max_tiempo))

