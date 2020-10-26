class Partida():
    def __init__(self, palabra, intentos=0, tipo_palabra='',
                 nombre_jugador='', palabra_aciertos=[]):
        self.palabra = palabra
        self.intentos = intentos
        self.tipo_palabra = tipo_palabra
        self.nombre_jugador = nombre_jugador
        self.palabra_aciertos = palabra_aciertos

    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, value):
        if bool(value.strip()) is True:
            self._palabra = list(value.upper())
        else:
            raise ValueError("La palabra no puede ser vacio")

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, value):
        if bool(value.strip()) is True:
            self._tipo_palabra = value.upper()
        else:
            raise ValueError("La palabra no puede ser vacio")

    @property
    def intentos(self):
        return self._intentos

    @intentos.setter
    def intentos(self, value):
        if value > 0:
            self._intentos = value
        else:
            raise ValueError("El numero de intentos no puede ser negativo")

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, value):
        if bool(value.strip()) is True:
            self._nombre_jugador = value.upper()
        else:
            raise ValueError("El jugador no puede ser vacio")

    @property
    def palabra_aciertos(self):
        return self._palabra_aciertos

    @palabra_aciertos.setter
    def palabra_aciertos(self, value):
        self._palabra_aciertos = [None]*len(self.palabra)
