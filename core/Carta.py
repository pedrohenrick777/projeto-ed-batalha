class Carta:
    '''Classe utilizada para gerar as cartas, guarda o valor, cor, número e naipe da respectiva carta'''
    def __init__(self, numero, naipe, cor, valor):
        self.__numero = numero
        self.__naipe = naipe
        self.__cor = cor
        self.__valor = valor

    @property
    def naipe(self):
        return self.__naipe

    @property
    def numero(self):
        return self.__numero

    @property
    def cor(self):
        return self.__cor

    @property
    def valor(self):
        return self.__valor

    def __str__(self):  # todas as informacoes da carta
        return f'{self.__numero} de {self.__naipe} {self.__cor} '

    def __repr__(self):  # todas as informacoes da carta
        return f'{self.__numero} de {self.__naipe} {self.__cor} '
