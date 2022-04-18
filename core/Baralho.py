# Baralho = coleçao de cartas (lista de cartas)
import random

from utils.PilhaEncadeada import Pilha, PilhaException

from core.Carta import Carta


class BaralhoVazioException(Exception):
    def __init__(self):
        super().__init__()


class Baralho:
    '''Baralho inicial, utilizado na distribuição de cada carta para os jogadores.'''
    def __init__(self):
        self.cartas = Pilha()
        for carta in self.gerar_baralho():
            self.cartas.empilha(carta)

    def retirarCarta(self) -> Carta:
        '''Função para retirar uma carta do baralho'''
        try:
            return self.cartas.desempilha()
        except PilhaException:
            raise BaralhoVazioException

    @staticmethod
    def embaralhar(cartas):
        '''função para embaralhar uma lista'''
        random.shuffle(cartas)
        return cartas

    def gerar_baralho(self):
        '''Gera as cartas e embaralha o baralho'''
        naipe = {"Ouro": "vermelho", "Espada": "preto", "Paus": "preto", "Copas": "vermelho"}
        numeracao = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "dama", "rei"]
        cartas_embaralhadas = []
        for nome_naipe, cor in naipe.items():
            for valor, id in enumerate(numeracao):
                cartas_embaralhadas.append(Carta(id, nome_naipe, cor, valor+1))
        cartas_embaralhadas = self.embaralhar(cartas_embaralhadas)
        return cartas_embaralhadas

    def __str__(self):
        '''função que imprime todas as cartas do baralho'''
        saida = ''
        for carta in self.baralho:
            saida += str(carta) + '\n'
        return saida
