from utils.PilhaEncadeada import *


class NomeJogadorException(Exception):
    """ Classe criada para retornar mensagens de exceções relacionadas ao Nome do Jogador """

    def __init__(self):
        super().__init__()


class JogadorSemCartasException(Exception):
    """ Classe criada para retornar mensagens de exceções relacionadas ao Jogador sem Cartas """

    def __init__(self):
        super().__init__()


class Jogador:
    """ Classe criada para representar o baralho do jogo

    Atributos
    _________
    nome:
        nome do jogador
    cartas:
        cartas do jogador
    cartas_pegas:
        cartas acumuladas pelo jogador no momento que ele ganha as rodadas

    """

    def __init__(self, nome):
        """ construtor padrão que inicializa o objeto Jogador """
        if nome == '':
            raise NomeJogadorException
        self.__nome = nome
        self.__cartas = Pilha()
        self.__cartas_pegas = Pilha()

    def pegarCartaOponente(self, carta):
        """Método que adiciona as cartas ganhas durante a rodada em uma pilha que será usada caso a pilha original de cartas do jogador chegue ao fim"""
        self.__cartas_pegas.empilha(carta)

    def retiraCarta(self):
        """Método que checa se o jogador tem cartas tanto na pilha original de cartas quanto na pilha de cartas ganhas nas rodadas, caso sim, retorna a carta do topo"""
        try:
            if not self.temCartas():
                while self.temCartasAcumuladas():
                    self.receberCartas(self.__cartas_pegas.desempilha())
            return self.__cartas.desempilha()
        except PilhaException:
            raise JogadorSemCartasException

    def receberCartas(self, carta):
        """Método que empilha as cartas recebidas"""
        self.__cartas.empilha(carta)

    def temCartas(self):
        """Método que retorna se existem cartas ou não"""
        return self.__cartas.tamanho() != 0

    def temCartasAcumuladas(self):
        """Método que retorna se existem cartas acumuladas ou não"""
        return self.__cartas_pegas.tamanho() != 0

    @property
    def cartas_pegas(self):
        """Método que retorna as cartas pegas"""
        return self.__cartas_pegas

    @property
    def cartas(self):
        """Método que retorna as cartas"""
        return self.__cartas

    @property
    def nome(self):
        """Método que retorna o nome do jogador"""
        return self.__nome

    @property
    def numeroCartas(self):
        """Método que retorna o numero de Cartas do jogador"""
        return self.__cartas.tamanho() + self.__cartas_pegas.tamanho()

    def __str__(self) -> str:
        """Método que retorna o nome do jogador"""
        return self.__nome
