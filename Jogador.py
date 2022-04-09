from utils.PilhaEncadeada import Pilha


class NomeJogadorException(Exception):
    def __init__(self, mensagem, metodo=''):
        super().__init__(mensagem)
        self.metodo = metodo

class Jogador:
    def __init__(self, nome):
        self.__nome = nome
        self.__cartas = Pilha()
        self.__cartas_acumuladas = []

    def pegarCartaOponente(self, carta):
        self.cartas_ganhas.insert(0, carta)

    def retiraCarta(self):
        carta = self.__cartas.desempilha()
        return carta

    def receberCartas(self, carta):
        self.__cartas.empilha(carta)

    def quantificarCartas(self):
        return self.__cartas.tamanho() + len(self.__cartas_acumuladas)

    def temCartasAcumuladas(self):
        return self.__cartas_acumuladas is None

    @property
    def cartas_ganhas(self):
        return self.__cartas_acumuladas
    @property
    def cartas(self):
        return self.__cartas 

    @property
    def nome(self):
        return self.__nome

    @property
    def numeroCartas(self):
        return len(self.__cartas)
    