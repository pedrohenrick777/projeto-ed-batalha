from utils.PilhaEncadeada import *


class NomeJogadorException(Exception):
    def __init__(self):
        super().__init__()

class JogadorSemCartasException(Exception):
    def __init__(self):
        super().__init__()

class Jogador:
    '''Gera um objeto jogador, que guarda suas cartas e seu nome'''
    def __init__(self, nome):
        if nome == '':
            raise NomeJogadorException
        self.__nome = nome
        self.__cartas = Pilha()
        self.__cartas_pegas = Pilha()

    def pegarCartaOponente(self, carta):
        '''Adiciona as cartas ganhas durante a rodada em uma pilha que será usada caso a pilha original de cartas do jogador chegue ao fim'''
        self.__cartas_pegas.empilha(carta)

    def retiraCarta(self):
        '''checa se o jogador tem cartas tanto na pilha original de cartas quanto na pilha de cartas ganhas nas rodadas, caso sim, retorna a carta do topo'''
        try:
            if not self.temCartas():
                while self.temCartasAcumuladas():
                    self.receberCartas(self.__cartas_pegas.desempilha())
            return self.__cartas.desempilha()
        except PilhaException:
            raise JogadorSemCartasException

    def receberCartas(self, carta):
        self.__cartas.empilha(carta)

    def temCartas(self):
        return self.__cartas.tamanho() != 0

    def temCartasAcumuladas(self):
        return self.__cartas_pegas.tamanho() != 0

    @property
    def cartas_pegas(self):
        return self.__cartas_pegas

    @property
    def cartas(self):
        return self.__cartas 

    @property
    def nome(self):
        return self.__nome

    @property
    def numeroCartas(self):
        return self.__cartas.tamanho() + self.__cartas_pegas.tamanho()
    
    def __str__(self) -> str:
        return self.__nome

    