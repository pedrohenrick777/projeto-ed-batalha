# Baralho = coleçao de cartas (lista de cartas)
import random
from core.Carta import Carta
from utils.PilhaEncadeada import Pilha, PilhaException


class BaralhoVazioException(Exception):
    """ Classe criada para retornar mensagens de exceções relacionadas ao Baralho """

    def __init__(self):
        """ Construtor padrão que inicializa a classe de exceção da pilha """
        super().__init__()


class Baralho:
    """ Classe criada para representar o baralho do jogo

    Atributo
    _________
    cartas:
        atributo que considera o último valor a ser empilhado

    """

    def __init__(self):
        """ construtor padrão que inicializa o objeto Baralho """
        self.cartas = Pilha()
        for carta in self.gerar_baralho():
            self.cartas.empilha(carta)

    def retirarCarta(self) -> Carta:
        """Método para retirar uma carta do baralho"""
        try:
            return self.cartas.desempilha()
        except PilhaException:
            raise BaralhoVazioException

    @staticmethod
    def embaralhar(cartas):
        """Método para embaralhar uma lista"""
        random.shuffle(cartas)
        return cartas

    def gerar_baralho(self):
        """Método para gerar as cartas e embaralhar o baralho"""
        naipe = {"Ouro": "vermelho", "Espada": "preto", "Paus": "preto", "Copas": "vermelho"}
        numeracao = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "dama", "rei"]
        cartas_embaralhadas = []
        for nome_naipe, cor in naipe.items():
            for valor, id in enumerate(numeracao):
                cartas_embaralhadas.append(Carta(id, nome_naipe, cor, valor + 1))
        cartas_embaralhadas = self.embaralhar(cartas_embaralhadas)
        return cartas_embaralhadas

    def __str__(self):
        """Método que retorna todas as cartas"""
        saida = ''
        for carta in self.baralho:
            saida += str(carta) + '\n'
        return saida
