import threading
import time

# Función que simula una tarea para un hilo
def tarea_hilo(identificador, Any):
    for i in range(9):
        print(f'Hilo {identificador}: Realizando tarea {i}')
        time.sleep(Any)

# Crear instancias de hilos
hilo1 = threading.Thread(target=tarea_hilo, args=( 1, 2))
hilo2 = threading.Thread(target=tarea_hilo, args=(2, 3.6))

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que los dos hilos terminen
hilo1.join()
hilo2.join()

print('Programa principal: Todas las tareas han sido completadas.')
