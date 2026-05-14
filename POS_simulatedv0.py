import time
import random
from collections import deque

# helpers
def separador(char="─", largo=52):
    print(char * largo)
 
def titulo(texto):
    print()
    separador("═")
    padding = (52 - len(texto) - 2) // 2
    print(f"{'═' * padding} {texto} {'═' * padding}")
    separador("═")
    print()

# Proceso simulado
class Proceso:
    def __init__(self, id, nombre, tiempo_ejecucion):
        self.id = id
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion
        self.estado = "Listo"

    def ejecutar(self):
        self.estado = "Ejecutando"
        print()
        separador(".")
        print(f"  ▶  Ejecutando proceso: {self.nombre} (ID: {self.id})...")
        print(f"     Duración estimada: {self.tiempo_ejecucion} segundos - Estado: {self.estado}")
        separador(".")

        # para simular una barra de progreso
        pasos = 20
        for i in range(pasos + 1):
            bloques    = "█" * i
            vacios     = "░" * (pasos - i)
            porcentaje = int((i / pasos) * 100)
            print(f"\r  [{bloques}{vacios}] {porcentaje:3d}%", end="", flush=True)
            time.sleep(self.tiempo_ejecucion / pasos)
 
        self.estado = "Terminado"
        print(f"\r  [{'█' * pasos}] 100%")
        print(f"  ✔  Proceso '{self.nombre}' finalizado - Estado: {self.estado}")

# Planificador (Scheduler) fifo
class Planificador:
    def __init__(self):
        self.cola = deque()
        self.procesos_ejecutados = []

    # se agrega el proceso al final de la cola
    def agregar_proceso(self, proceso):
        self.cola.append(proceso)
        print(f"  ✔  Proceso '{proceso.nombre}' (ID: {proceso.id}) agregado a la cola FIFO - Estado: {proceso.estado}")

    def mostrar_cola(self):
        titulo("Cola de Procesos FIFO")
        if not self.cola:
            print("  ⚠  La cola de procesos está vacía.")
            return
        for pos, proceso in enumerate(self.cola, start=1):
            print(f"  {pos}. {proceso.nombre} (ID: {proceso.id} - Tiempo: {proceso.tiempo_ejecucion}s - Estado: {proceso.estado})")
        separador()

    def ejecutar(self):
        titulo("Ejecución FIFO")
        if not self.cola:
            print("  ⚠  No hay procesos para ejecutar.")
            return
        
        total = len(self.cola)
        print(f"  ▶  Procesos en cola: {total} - Algoritmo FIFO")
        turno = 1

        while self.cola:
            proceso = self.cola.popleft() #toma el primero
            print(f"\n  Turno {turno}/{total} - {proceso.nombre} (ID: {proceso.id})")
            proceso.ejecutar()
            self.procesos_ejecutados.append(proceso)
            turno += 1
        
        print()
        titulo("Ejecución Completa")
        print(f"  ✔  Todos los procesos han finalizado.")
        print("  ▶  Orden de ejecución:")
        for pos, proceso in enumerate(self.procesos_ejecutados, start=1):
            print(f"  {pos}. {proceso.nombre} (ID: {proceso.id})")

# Simulación de memoria
mem_total = 512 # MB

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

def menu():
    print("""
    ┌─────────────────────────────────────────┐
    │             MENÚ PRINCIPAL              │
    ├─────────────────────────────────────────┤
    │  1  Crear proceso                       │
    │  2  Ver cola de procesos                │
    │  3  Ejecutar todos los procesos (FIFO)  │
    │  4  Asignar memoria a proceso           │
    │  5  Liberar memoria de proceso          │
    │  6  Salir                               │
    └─────────────────────────────────────────┘""")

# Interfaz de usuario (CLI)
def interfaz_usuario():
    titulo("Simulador de Sistema Operativo Básico")
    print("  ▶  Algoritmo de Planificación: FIFO (First In, First Out)")
    print(f"  ▶  Memoria total disponible: {mem_total} MB")
    print()
    planificador = Planificador()
    memoria = Memoria()

    while True:
        menu()
        opcion = input("  Opción: ").strip()

        if opcion == '1':
            titulo("Crear Proceso")
            id_proceso = input("Introduce ID del proceso: ")
            nombre = input("Introduce nombre del proceso: ")
            tiempo_ejecucion = random.randint(1, 5)
            proceso = Proceso(id_proceso, nombre, tiempo_ejecucion)
            planificador.agregar_proceso(proceso)
        
        elif opcion == '2':
            print()
            planificador.mostrar_cola()

        elif opcion == '3':
            titulo("Ejecutar Procesos")
            planificador.ejecutar()

        elif opcion == '4':
            titulo("Asignar Memoria")
            id_proceso = input("Introduce ID del proceso: ")
            tamaño = int(input("Introduce el tamaño de memoria (MB): "))
            while tamaño > mem_total:
                print(f"  ⚠  El tamaño excede la memoria total disponible ({mem_total} MB). Intenta de nuevo.")
                tamaño = int(input("Introduce el tamaño de memoria (MB): "))
            memoria.asignar_memoria(id_proceso, tamaño)

        elif opcion == '5':
            titulo("Liberar Memoria")
            id_proceso = input("Introduce ID del proceso: ")
            memoria.liberar_memoria(id_proceso)

        elif opcion == '6':
            titulo("Cerrando Simulador")
            print("  ▶  Saliendo del sistema... ¡Hasta luego!")
            separador("═")
            break

        else:
            print()
            print("  ⚠  Opción no válida. Elige un número del 1 al 6.")

if __name__ == "__main__":
    interfaz_usuario()
