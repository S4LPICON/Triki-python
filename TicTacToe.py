#import random                                           #importaciones necesarias para la asignacion de jugadores aleatoria
import msvcrt                                            #importacion para que el usuario al presionar un tecla y haber finalizado el juego cierre la pestaña

def imprimir_tablero(tablero):
  print(" ")
  for i, fila in enumerate(tablero):
    print("  " + " | ".join(fila))          #Se hizo una optimizacion de la representacion del tablero
    if i < 2:
      print(" ---" * 3)
    else:
      print(" ")


def verificar_victoria(tablero, jugador):
  for fila in tablero:
    if all([c == jugador for c in fila]):               #cada vez que se hace una jugada se verifica si hubo ganador
      return True

  for col in range(3):
    if all([tablero[f][col] == jugador for f in range(3)]):                 #Gestionamiento de la matriz de juego
      return True

  if all([tablero[i][i] == jugador for i in range(3)]) or all(
    [tablero[i][2 - i] == jugador for i in range(3)]):
    return True

  return False


def tablero_lleno(tablero):
  return all([c != " " for fila in tablero for c in fila])        #verifica unicamente si el tablero esta lleno verificando los espacios en blanco


def jugar():
  tablero = [[" " for _ in range(3)] for _ in range(3)]         #asignacion de fichas al jugador (en orden por el momento)
  jugadores = ["X", "O"]
  turno_actual = 0

  print("╔══════════════════════╗")
  print("║   ¡Bienvenido a      ║")                           #un mensaje de bienvenida se ejecuta al iniciar el programa
  print("║    Tic Tac Toe!      ║")
  print("╚══════════════════════╝")

  while True:
    jugador_actual = jugadores[turno_actual]                                    #asigna la ficha al primer jugador 
    imprimir_tablero(tablero)                                                       #imprime el tablero inicial
    try:
      fila = int(
        input(f"➢ Jugador {jugador_actual}, elige una fila (1, 2, 3): ")) - 1
      col = int(                                                                                         #mensajes para los turnos de jugadores
        input(f"➢ Jugador {jugador_actual}, elige una columna (1, 2, 3): ")) - 1

      if 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == " ":
        tablero[fila][col] = jugador_actual
        if verificar_victoria(tablero, jugador_actual):
          imprimir_tablero(tablero)
          print(f"╔══════════════════════╗")
          print(f"║ ¡Jugador {jugador_actual} gana!     ║")                                   #usando las varibles de jugadores podemos saber cual fue el ultimo turno
          print(f"╚══════════════════════╝")                                                  #si alguien resulta ganador, normalmente es el ultimo que jugó
          break
        elif tablero_lleno(tablero):
          imprimir_tablero(tablero)
          print("╔══════════════════════╗")                                                         #aqui se comprueba el tablero lleno y verifica si hubo ganador
          print("║      ¡Empate!        ║")                                                         #si se lleno el tablero y no hubo ganador significa que hay un empate
          print("╚══════════════════════╝")
          break
        else:
          turno_actual = 1 - turno_actual
      else:
        print("Por favor, elige una casilla válida.")                                           #mensajes de error para cuando un jugador ingresa valores invalidos
    except ValueError:                                                                          # ó la casilla ya esta ocupada
      print("Ingresa valores numéricos válidos.")


if __name__ == "__main__":
  jugar()                                                                    #se convirtio a funcion por temas de compatibilidad mia a otras aplicaciones
  print("Presione una tecla para cerrar...")                                  #al terminar la partida (ya sea si se empató o hubo un ganador) para cerrar la 
  msvcrt.getch()                                                              #pestaña requiere que el usuario presione una tecla sin importa cual sea
