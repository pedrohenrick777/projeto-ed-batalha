import os
from itertools import count
from time import sleep

from Baralho import Baralho
from Jogador import *
from utils.CompararCartas import *
from utils.PilhaEncadeada import PilhaException


def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    while True:
        limpar_tela()
        try:
            nome_jogador_1 = input('Nome do Jogador 1: ').strip()
            nome_jogador_2 = input('Nome do Jogador 2: ').strip()
            if not nome_jogador_1 or not nome_jogador_2:
                raise NomeJogadorException('Digite o nome dos jogadores!')
        except NomeJogadorException as e:
            print(e, 'Enter para continuar')
            input('')
            continue

        jogador_1 = Jogador(nome_jogador_1)
        jogador_2 = Jogador(nome_jogador_2)
        print(f'Olá {str(jogador_1.nome)} e {jogador_2.nome}!!!')
        print(f'Vamos começar embaralhando as cartas...')
        baralho = Baralho()
        for n in count():
            try:
                if n % 2 == 0:
                    jogador_1.receberCartas(baralho.retirarCarta())
                else:
                    jogador_2.receberCartas(baralho.retirarCarta())
            except PilhaException:
                break
        sleep(4)
        carta_j1 = jogador_1.retiraCarta()
        carta_j2 = jogador_2.retiraCarta()
        print(f'\n{carta_j1} x {carta_j2}')
        print(comparar_cartas(carta_j1, carta_j2))
        input()

if __name__ == '__main__':
    main()
