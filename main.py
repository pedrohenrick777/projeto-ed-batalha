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


def receber_cartas(jogador_1, jogador_2, baralho):
    for n in count():
        try:
            if n % 2 == 0:
                jogador_1.receberCartas(baralho.retirarCarta())
            else:
                jogador_2.receberCartas(baralho.retirarCarta())
        except PilhaException:
            break


def main():
    rodada=0
    while True:
        try:
            nome_jogador_1 = input('Nome do Jogador 1: ').strip()
            nome_jogador_2 = input('Nome do Jogador 2: ').strip()
            rodada_fim = int(input('Digite a quantidade máxima de rodadas: '))
            if not nome_jogador_1 or not nome_jogador_2:
                raise NomeJogadorException('Digite o nome dos jogadores!')
            else:
                break
        except NomeJogadorException as e:
            print(e, 'Enter para continuar')
            input('')
            continue
    jogador_1 = Jogador(nome_jogador_1)
    jogador_2 = Jogador(nome_jogador_2)
    print(f'Olá {jogador_1.nome} e {jogador_2.nome}!!!')
    print(f'Vamos começar embaralhando as cartas...')
    baralho = Baralho()

    while True:
        acumulado = []
        rodada +=1
        limpar_tela()
        receber_cartas(jogador_1=jogador_1, jogador_2=jogador_2, baralho=baralho)
        sleep(1)
        carta_j1 = jogador_1.retiraCarta()
        carta_j2 = jogador_2.retiraCarta()
        print(f'\nA carta do {jogador_1.nome} é:\n{carta_j1}\nA carta do {jogador_2.nome} é: \n{carta_j2}')

        while verificarEmpate(carta_j1.valor, carta_j2.valor):
            resultado, acumulado, jogadas1, jogadas2 = comparar_cartas(carta_j1, carta_j2, acumulado)
            print(resultado)
            print(f'As cartas acumuladas são: {acumulado}')
            input()
            if jogador_2.cartas.estaVazia():
                if len(jogador_2.cartas_ganhas) != 0:
                    for carta in jogador_2.cartas_ganhas:
                        jogador_2.cartas.empilha(carta)
                        jogador_2.cartas_ganhas.pop(0)
                else:
                    print(f'Acabou o jogo! {jogador_1.nome} ganhou e {jogador_2.nome} não possui mais cartas depois desse empate.')
                    break
            if jogador_1.cartas.estaVazia():
                if len(jogador_1.cartas_ganhas) != 0:
                    for carta in jogador_1.cartas_ganhas:
                        jogador_1.cartas.empilha(carta)
                        jogador_1.cartas_ganhas.pop(0)
                else:
                    print(f'Acabou o jogo! {jogador_2.nome} ganhou e {jogador_1.nome} não possui mais cartas depois desse empate.')
                break
            carta_j1 = jogador_1.retiraCarta()
            carta_j2 = jogador_2.retiraCarta()

        resultado, acumulado, jogadas1, jogadas2 = comparar_cartas(carta_j1, carta_j2, acumulado)

        if jogadas1 == "perdeu":
            for lista in jogadas2:
                jogador_2.pegarCartaOponente(lista)
            print(f'{jogador_1.nome} perdeu a rodada {rodada}')
        if jogadas2 == "perdeu":
            for lista in jogadas1:
                jogador_1.pegarCartaOponente(lista)
            print(f'{jogador_2.nome} perdeu a rodada {rodada}')
        print(f'O {jogador_1.nome} possui {jogador_1.quantificarCartas()} cartas!\nO jogador 2 possui {jogador_2.quantificarCartas()} cartas!')
        if jogador_1.cartas.estaVazia():
            if len(jogador_1.cartas_ganhas) != 0:
                for carta in jogador_1.cartas_ganhas:
                    jogador_1.cartas.empilha(carta)
                    jogador_1.cartas_ganhas.pop(0)
            else:
                print(f'{jogador_2.nome} venceu o jogo')
                break
        if jogador_2.cartas.estaVazia():
            if len(jogador_2.cartas_ganhas) != 0:
                for carta in jogador_2.cartas_ganhas:
                    jogador_2.cartas.empilha(carta)
                    jogador_2.cartas_ganhas.pop(0)
            else:
                print(f'{jogador_1.nome} venceu o jogo')
                break
        else:
            if rodada >= rodada_fim:
                if jogador_1.quantificarCartas() > jogador_2.quantificarCartas():
                    print(f'{jogador_1.nome} é o ganhador!')
                    break
                elif jogador_1.quantificarCartas() < jogador_2.quantificarCartas():
                    print(f'{jogador_2.nome} é o ganhador!')
                    break
                else:
                    pass


            print("\n##########################\nVamos para mais uma rodada!\n##########################")
            input()


if __name__ == '__main__':
    main()
