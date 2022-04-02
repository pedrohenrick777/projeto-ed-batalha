class NomeJogadorException(Exception):
    def __init__(self, mensagem, metodo=''):
        super().__init__(mensagem)
        self.metodo = metodo

class Jogador:
    def __init__(self, nome):
        self.__nome = nome
        self.__cartas = []
        self.__cartas_retiradas = []

    def devolverCarta(self, cartas_a_devolver:list):
        for carta in cartas_a_devolver:
            self.__cartas.insert(0, carta)

    def retiraCarta(self):
        carta = self.__cartas.pop()
        return carta

    def receberCartas(self, carta):
        self.__cartas.append(carta)

    @property
    def cartas_retiradas(self):
        return self.__cartas_retiradas

    @property
    def cartas(self):
        return self.__cartas 

    @property
    def nome(self):
        return self.__nome

    def numeroCartas(self):
        return len(self.__cartas)
    