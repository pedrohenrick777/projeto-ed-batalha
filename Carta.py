class Carta:

    def __init__(self, numero, naipe, cor):
        self.__numero = numero
        self.__naipe = naipe
        self.__cor = cor

    @property
    def naipe(self):
        return self.__naipe

    @property
    def numero(self):
        return self.__numero

    @property
    def numero(self):
        return self.__cor

    def __str__(self):  # todas as informacoes da carta
        return f'{self.__numero} de {self.__naipe} de {self.__cor} '
