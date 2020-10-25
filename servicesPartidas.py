from repositorios import Repositorios
from partida import Partida
import random


class ServicesPartidas():
    # Esta funcion saca deuelve la ultima key del repositorio que le pasemos
    def get_last_key(self, diccionario):
        lastKey = -1
        for key in diccionario:
            lastKey = key
        return(lastKey)

    # Esta deuvelve una palabra del repositorio elegida al azar
    def get_random_palabra(self):
        fin_rango = self.get_last_key(Repositorios.palabrasList)
        indice_palabra = random.randrange(0, fin_rango)
        palabra_generada = Repositorios.palabrasList[indice_palabra]
        return palabra_generada

    # Esta funcion guarda una palabra ingresada en el repositorio
    # de palabras que puede elegir la funcion random
    # si es que la palabra no existe ya en el repositorio
    # de ser asi devuelve un mensaje diciendo que ya existe

    def guardar_palabra(self, palabra, tipo):
        palabra_a_guardar = {}
        palabra_a_guardar['palabra'] = palabra
        palabra_a_guardar['tipo_palabra'] = tipo
        new_key = int(self.get_last_key(Repositorios.palabrasList)) + 1
        verificador = True
        for key in Repositorios().palabrasList:
            if Repositorios().palabrasList[key]['palabra'] == palabra:
                verificador = False
        if verificador is True:
            Repositorios().palabrasList[new_key] = palabra_a_guardar
            return "La palabra se guardo"
        else:
            return "La palabra ya estaba guardada"

    def guardar_partida(self, nombre, resultado, palabra,
                        letras_adivinadas, intentos_restantes):
        partida_a_guardar = {}
        partida_a_guardar['Nombre del jugador'] = nombre
        partida_a_guardar['Resultado de la partida'] = resultado
        partida_a_guardar['Palabra que debia adivinar'] = palabra
        partida_a_guardar['Letras que adivino'] = letras_adivinadas
        partida_a_guardar['Intentos que le quedaron'] = intentos_restantes
        new_key = int(self.get_last_key(Repositorios.partidasList)) + 1
        Repositorios().partidasList[new_key] = partida_a_guardar

    def iniciar_partida(self, nombre, dificultad, palabra, tipo_palabra):
        # Se verifica que el nombre del jugador no este vacio
        if bool(str(nombre).strip()) is False:
            raise ValueError("Se debe ingresar un nombre de jugador")
        # Esta parte verifica si palabra y tipo de palabra estan vacios\
        # para asignarles un valor de forma autmatica
        # De lo contrario se verifica que se hayan ingresado ambos
        if (bool(palabra) is False and
           bool(tipo_palabra) is False):
            palabra_random = self.get_random_palabra()
            palabra = palabra_random['palabra']
            tipo_palabra = palabra_random['tipo_palabra']
        elif (bool(palabra.strip()) is True and
              bool(tipo_palabra.strip()) is False):
            raise ValueError("Se ingreso una palabra pero no el tipo")
        elif (bool(palabra.strip()) is False and
              bool(tipo_palabra.strip()) is True):
            raise ValueError("NO se ingreso una palabra pero si el tipo")
        # Esta parte verifica que la dificultad ingresada no
        # este fuera del rango (1,10) y calcula la cantidad de intentos
        # que tendra el jugador segun la dificultad y el largo de la palabra
        if dificultad < 0 or dificultad > 10:
            raise ValueError("La dificultad ingresada no esta entre 1 y 10")
        else:
            intentos = dificultad*len(palabra)

        return Partida(palabra, intentos, tipo_palabra, nombre)

    def intentar_letra(self, partida, letra):
        letra = letra.upper()
        key = 0
        if partida._intentos != 0:
            for letter in partida._palabra:
                if letra == letter:
                    partida._palabra_aciertos[key] = letra
                key += 1
            partida._intentos -= 1
            if partida._palabra == partida._palabra_aciertos:
                return 'Gano'
            elif partida._intentos == 0:
                return 'Perdio'
            else:
                return 'Continua'
        else:
            raise ValueError("Ya no le quedan intentos")
