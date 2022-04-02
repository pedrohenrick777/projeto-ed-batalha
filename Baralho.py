# Baralho = coleçao de cartas (lista de cartas)
import random

from Carta import Carta
from utils.PilhaEncadeada import Pilha


class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Baralho:
    def __init__(self):
        self.cartas = Pilha()
        naipe = ["Ouro", "Espada", "Paus", "Copas"]
        cor = ["vermelho", "preto", "preto", "vermelho"]
        numeracao = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "dama", "rei"]
        cartas_embaralhadas = []
        for idx in range(len(naipe)):
            for valor, id in enumerate(numeracao):
                cartas_embaralhadas.append(Carta(id, naipe[idx], cor[idx], valor+1))
        cartas_embaralhadas = self.embaralhar(cartas_embaralhadas)

        for carta in cartas_embaralhadas:
            self.cartas.empilha(carta)

    """ def __len__(self):
        return len(self.baralho)

    def temCarta(self):
        if len(self.baralho) > 0:
            return True
        else:
            return False """

    def retirarCarta(self) -> Carta:
        try:
            return self.cartas.desempilha()
        except IndexError:
            raise BaralhoException('O baralho está vazio. Não há cartas para retirar')

    def embaralhar(self, cartas):
        random.shuffle(cartas)
        return cartas

    """ def dividir_baralho(self):
        cartas_jogador_1 = []
        cartas_jogador_2 = []
        self.embaralhar()
        for num, carta in enumerate(self.baralho):
            if num % 2 == 0:
                cartas_jogador_1.append(carta)
            else:
                cartas_jogador_2.append(carta)
        
        return cartas_jogador_1, cartas_jogador_2 """

    def __str__(self):
        saida = ''
        for carta in self.baralho:
            saida += carta.__str__() + '\n'
        return saida
