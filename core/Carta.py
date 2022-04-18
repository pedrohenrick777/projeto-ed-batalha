class Carta:
    """Classe utilizada para gerar as cartas, guarda o valor, cor, número e naipe da respectiva carta

    Atributos
    _________
    numero:
        representa o número da carta
    naipe:
        representa o naipe da carta
    cor:
        representa a cor da carta
    valor:
        representa o valor da carta
    """

    def __init__(self, numero, naipe, cor, valor):
        """ construtor padrão que inicializa o objeto Carta """
        self.__numero = numero
        self.__naipe = naipe
        self.__cor = cor
        self.__valor = valor

    @property
    def naipe(self):
        """Método para retornar o naipe da carta"""
        return self.__naipe

    @property
    def numero(self):
        """Método para retornar o número da carta"""
        return self.__numero

    @property
    def cor(self):
        """Método para retornar a cor da carta"""
        return self.__cor

    @property
    def valor(self):
        """Método para retornar o valor da carta"""
        return self.__valor

    def __str__(self):  # todas as informacoes da carta
        """Método para retornar todas as informações da carta """
        return f'{self.__numero} de {self.__naipe} {self.__cor} '

    def __repr__(self):  # todas as informacoes da carta
        return f'{self.__numero} de {self.__naipe} {self.__cor} '
