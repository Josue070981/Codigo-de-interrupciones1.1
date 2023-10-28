import random
import time

# Función para generar números aleatorios
def generar_numeros_aleatorios(minimo, maximo):
    return random.randint(minimo, maximo)

# Función para realizar una operación (resta, suma, multiplicación, división)
def operacion_numeros(operacion, tiempo_limite):
    start_time = time.time()
    print(f"Iniciando operación de {operacion} durante {tiempo_limite} segundos.")
    while time.time() - start_time < tiempo_limite:
        numero1 = generar_numeros_aleatorios(1, 100)
        numero2 = generar_numeros_aleatorios(1, 100)
        resultado = None  # Inicializamos resultado con None

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

# Define el rango de tiempo para cada operación
min_tiempo = 5  # Tiempo mínimo en segundos
max_tiempo = 15  # Tiempo máximo en segundos

# Realiza las operaciones en el orden deseado con tiempos aleatorios
operacion_numeros("resta", random.uniform(min_tiempo, max_tiempo))
operacion_numeros("suma", random.uniform(min_tiempo, max_tiempo))
operacion_numeros("division", random.uniform(min_tiempo, max_tiempo))
operacion_numeros("multiplicacion", random.uniform(min_tiempo, max_tiempo))
