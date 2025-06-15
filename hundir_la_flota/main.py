from utils import crea_tablero, colocar_barcos, recibir_disparo
import random

"""
Comprueba si aún quedan barcos en el tablero ("O"). Esencial para saber cuándo termina la partida.
"""

def hay_barcos(tablero):
    return (tablero == "O").any()




"""
Crea los tableros de jugador y de máquina.

Coloca las naves automáticamente.

Se turnan hasta que alguien gana.

Muestra el tablero de jugador en cada ronda.


Organiza el flujo principal del juego, conectando todas las demás funciones en un orden lógico.

"""

def main():
    tab_jugador = colocar_barcos(crea_tablero())
    tab_maquina = colocar_barcos(crea_tablero())

    while True:
        print("Tu tablero:")
        mostrar_tablero(tab_jugador) 

        turno_jugador(tab_maquina)
        if not hay_barcos(tab_maquina):
            print("Felicitaciones, ganaste!")
            break

        turno_maquina(tab_jugador)
        if not hay_barcos(tab_jugador):
            print("La máquina ganó! Inténtalo de nuevo.")
            break



"""
Solicita al jugador las coordenadas del disparo.

Convierte la cadena en una tupla de enteros.

Llama a recibir_disparo para ejecutar el disparo en el tablero de la máquina.


Permite al jugador interactuar con el juego y elegir dónde atacar. Esencial para la jugabilidad.

"""

def turno_jugador(tablero_maquina):
    
    disparo_coordenada = input("Coordenadas para el disparo: ")
    disparo_coordenada = disparo_coordenada.split(",")
    for x, y in enumerate(disparo_coordenada):
        disparo_coordenada[x] = int(y)
    disparo_coordenada = tuple(disparo_coordenada)
    print(disparo_coordenada)
    recibir_disparo(tablero_maquina, disparo_coordenada)



"""

Genera un tiro aleatorio con coordenadas válidas.

Determinar el tamaño del tablero del jugador

La máquina elige dos números aleatorios

Dispara al tablero del jugador.

Llama a la función recibir_disparo, que verifica qué sucede en la coordenada seleccionada:

Si impacta un barco ("O"), lo marca como "X" (impacto).

Si ya había sido impactado, avisa de que lo está siendo de nuevo.

Si no impactó nada, lo marca con "-" guión.

También imprime el mensaje correspondiente en pantalla 

"""
def turno_maquina(tablero_jugador):
     i = tablero_jugador.shape[0] # lineas
     j = tablero_jugador.shape[1] # columnas

     while True:
        disparo_maquina = (random.randint(0,i-1),random.randint(0, j -1))
        
        recibir_disparo(tablero_jugador, disparo_maquina)
        break



"""
Muestra el tablero del jugador en la consola, línea por línea.

Permite al jugador ver el estado actual de su tablero: dónde están sus naves, cuántos disparos ha recibido.
"""
def mostrar_tablero(tablero):
    
    for fila in tablero:
        print(" ".join(fila))
    print()  


"""
Ejecuta la función main() solo si el archivo se ejecuta directamente (no se importa como módulo).
"""

main()
