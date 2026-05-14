import time
import random

# Proceso simulado
class Proceso:
    def __init__(self, id, nombre, tiempo_ejecucion):
        self.id = id
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion
        self.estado = "Listo"

    def ejecutar(self):
        print(f"Ejecutando proceso {self.nombre}...")
        time.sleep(self.tiempo_ejecucion)
        self.estado = "Terminado"
        print(f"Proceso {self.nombre} terminado.")

# Planificador (Scheduler)
class Planificador:
    def __init__(self):
        self.procesos = []
        self.procesos_ejecutados = []

    def agregar_proceso(self, proceso):
        self.procesos.append(proceso)

    def ejecutar(self):
        while self.procesos:
            proceso = self.procesos.pop(0)
            proceso.ejecutar()
            self.procesos_ejecutados.append(proceso)

# Simulación de memoria
class Memoria:
    def __init__(self):
        self.memoria = {}

    def asignar_memoria(self, id_proceso, tamaño):
        if id_proceso in self.memoria:
            print(f"Memoria ya asignada al proceso {id_proceso}.")
        else:
            self.memoria[id_proceso] = tamaño
            print(f"Memoria asignada al proceso {id_proceso}, tamaño: {tamaño} MB.")

    def liberar_memoria(self, id_proceso):
        if id_proceso in self.memoria:
            del self.memoria[id_proceso]
            print(f"Memoria liberada para el proceso {id_proceso}.")
        else:
            print(f"No se encontró memoria asignada al proceso {id_proceso}.")

# Interfaz de usuario (CLI)
def interfaz_usuario():
    planificador = Planificador()
    memoria = Memoria()

    while True:
        print("\nSistema Operativo Simulado")
        print("1. Crear proceso")
        print("2. Ejecutar procesos")
        print("3. Asignar memoria a proceso")
        print("4. Liberar memoria de proceso")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_proceso = input("Introduce ID del proceso: ")
            nombre = input("Introduce nombre del proceso: ")
            tiempo_ejecucion = random.randint(1, 5)
            proceso = Proceso(id_proceso, nombre, tiempo_ejecucion)
            planificador.agregar_proceso(proceso)
            print(f"Proceso {nombre} agregado.")
        
        elif opcion == '2':
            print("\nEjecutando todos los procesos en la cola...")
            planificador.ejecutar()

        elif opcion == '3':
            id_proceso = input("Introduce ID del proceso para asignar memoria: ")
            tamaño = int(input("Introduce el tamaño de memoria (MB): "))
            memoria.asignar_memoria(id_proceso, tamaño)

        elif opcion == '4':
            id_proceso = input("Introduce ID del proceso para liberar memoria: ")
            memoria.liberar_memoria(id_proceso)

        elif opcion == '5':
            print("Saliendo del sistema operativo simulado.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    interfaz_usuario()
