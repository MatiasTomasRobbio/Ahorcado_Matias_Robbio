from servicesPartidas import ServicesPartidas
from repositorios import Repositorios


class Ahorcado():
    def un_jugador(self):
        nombre = str(input("Ingrese el nombre del jugador: "))
        dificultad = int(input("Ingrese la dificultad[1,10]: "))
        game1 = ServicesPartidas().iniciar_partida(nombre, dificultad, '', '')
        flag1 = 'Continua'
        while flag1 == 'Continua':
            print("---------------------------------")
            print("Jugador: " + game1._nombre_jugador)
            print("Pista: " + game1._tipo_palabra)
            print("Intentos restantes:" + str(game1._intentos))
            letra = str(input("Ingrese una letra: "))
            if letra == 'salir':
                print('Usted ha finalizado el juego')
                flag1 = 'Perdio'
                break
            flag1 = ServicesPartidas().intentar_letra(game1, letra)
            print("Aciertos: " + str(game1._palabra_aciertos))
            print(flag1)
            print("---------------------------------")
        if flag1 == 'Gano' or flag1 == 'Perdio':
            ServicesPartidas().guardar_partida(game1._nombre_jugador,
                                               flag1,
                                               game1._palabra,
                                               game1._palabra_aciertos,
                                               game1._intentos)
            return True
        else:
            raise ValueError

    def dos_jugadores(self):
        print("Ahora juega jugador 1")
        nombre1 = str(input("Ingrese el nombre del jugador 1: "))
        dificultad1 = int(input("Ingrese la dificultad[1,10]: "))
        palabra_adivinar1 = str(input("Jugador 2 ingrese la palabra que"
                                      "debera adivinar jugador 1: "))
        tipo_plabra1 = str(input("Jugador 2 ingrese el tipo"
                                 "de palabra que es: "))
        game1 = ServicesPartidas().iniciar_partida(nombre1,
                                                   dificultad1,
                                                   palabra_adivinar1,
                                                   tipo_plabra1)
        flag1 = 'Continua'
        while flag1 == 'Continua':
            print("---------------------------------")
            print("Jugador 1: " + game1._nombre_jugador)
            print("Pista: " + game1._tipo_palabra)
            print("Intentos restantes:" + str(game1._intentos))
            letra = str(input("Ingrese una letra: "))
            if letra == 'salir':
                print('Jugador 1 ha finalizado el juego')
                flag1 = 'Perdio'
                break
            flag1 = ServicesPartidas().intentar_letra(game1, letra)
            print("Aciertos: " + str(game1._palabra_aciertos))
            print("Jugador 1 : " + flag1)
            print("---------------------------------")
        print("Ahora juega jugador 2")
        nombre2 = str(input("Ingrese el nombre del jugador 2: "))
        dificultad2 = int(input("Ingrese la dificultad[1,10]: "))
        palabra_adivinar2 = str(input("Jugador 1 ingrese la palabra que"
                                      "debera adivinar jugador 2: "))
        tipo_plabra2 = str(input("Jugador 1 ingrese el tipo"
                                 "de palabra que es: "))
        game2 = ServicesPartidas().iniciar_partida(nombre2,
                                                   dificultad2,
                                                   palabra_adivinar2,
                                                   tipo_plabra2)
        flag2 = 'Continua'
        while flag2 == 'Continua':
            print("---------------------------------")
            print("Jugador 2: " + game2._nombre_jugador)
            print("Pista: " + game2._tipo_palabra)
            print("Intentos restantes:" + str(game2._intentos))
            letra = str(input("Ingrese una letra: "))
            if letra == 'salir':
                print('Jugador 2 ha finalizado el juego')
                flag2 = 'Perdio'
                break
            flag2 = ServicesPartidas().intentar_letra(game2, letra)
            print("Aciertos: " + str(game2._palabra_aciertos))
            print("Jugador 2 : " + flag2)
            print("---------------------------------")
        # Se verifica si ambos terminaron y guarda las palabras que
        # ingresaron en palabrasList y ademas guarda la partida de
        # ambos en partidasList
        if ((flag1 == 'Gano' or flag1 == 'Perdio')
           and (flag2 == 'Gano' or flag2 == 'Perdio')):
            ServicesPartidas().guardar_palabra(game1._palabra,
                                               game1._tipo_palabra)
            ServicesPartidas().guardar_palabra(game2._palabra,
                                               game2._tipo_palabra)
            ServicesPartidas().guardar_partida(game1._nombre_jugador,
                                               flag1,
                                               game1._palabra,
                                               game1._palabra_aciertos,
                                               game1._intentos)
            ServicesPartidas().guardar_partida(game2._nombre_jugador,
                                               flag2,
                                               game2._palabra,
                                               game2._palabra_aciertos,
                                               game2._intentos)
            return True
        else:
            raise ValueError


if __name__ == '__main__':
    while True:
        print("####MENU AHORCADO######")
        print("1.Jugar \n2.Otras Opciones\n3.Salir")
        opcion = int(input("Seleccione una opcion"))
        if opcion == 1:
            print("1.Un jugador \n2.Dos jugadores")
            opcion = int(input("Seleccione una opcion"))
            if opcion == 1:
                Ahorcado().un_jugador()
            elif opcion == 2:
                Ahorcado().dos_jugadores()
        elif opcion == 2:
            print("1.Ver historial de partidas\n"
                  "2.Agregar una palabra al repositrio\n"
                  "3.Ver lista de palabras\n"
                  "4.Salir")
            opcion = int(input("Seleccione una opcion"))
            if opcion == 1:
                print("###HISTORIAL DE PARTIDAS###")
                historial = Repositorios().partidasList
                print(historial)
            elif opcion == 2:
                print("###AGREGAR PALABRA###")
                palabra = str(input("Ingrese la palabra"))
                tipo = str(input("Ingrese el tipo de palabra"))
                print(ServicesPartidas().guardar_palabra(palabra, tipo))
            elif opcion == 3:
                print("###LSITA DE PALABRAS###")
                print(Repositorios().palabrasList)
            elif opcion == 4:
                break
        elif opcion == 3:
            print("Fin del juego....")
            break
