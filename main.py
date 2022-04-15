import os
from Baralho import Baralho
from Jogador import *
from itertools import count
from time import sleep
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


def verificarOponenteCampeao(jogador):
    if jogador.cartas.estaVazia():
        if len(jogador.cartas_acumuladas) == 0:
            return True
        else:
            return False


def main():
    trocar_nome = True
    while True:
        rodada_fim = 0
        novo_jogo = ''
        confirma_troca_nome = ''

        try:
            if trocar_nome:
                nome_jogador_1 = input('Nome do Jogador 1: ').strip()
                nome_jogador_2 = input('Nome do Jogador 2: ').strip()
            if not nome_jogador_1 or not nome_jogador_2:
                raise NomeJogadorException('Digite o nome dos 2 jogadores!')
            while rodada_fim <= 0:

                try:
                    rodada = 0
                    rodada_fim = int(input('Digite a quantidade máxima de rodadas e pressione ENTER: '))
                    assert rodada_fim > 0

                except ValueError:
                    print('Digite um número inteiro válido')

                except AssertionError:
                    print('Digite um número maior que 0')

                except KeyboardInterrupt:
                    print('Leitura de dados interrompida pelo usuário')

        except KeyboardInterrupt:
            print('Leitura de dados interrompida pelo usuário')
            
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
            rodada += 1
            receber_cartas(jogador_1=jogador_1, jogador_2=jogador_2, baralho=baralho)
            carta_j1 = jogador_1.retiraCarta()
            carta_j2 = jogador_2.retiraCarta()
            print(f'\n~~~~~~~ RODADA {rodada} ~~~~~~~')
            print(f'\nA carta de {jogador_1.nome} é: {carta_j1}\nA carta de {jogador_2.nome} é: {carta_j2}')

            while verificarEmpate(carta_j1.valor, carta_j2.valor):
                resultado, acumulado, jogadas1, jogadas2 = compararCartas(carta_j1, carta_j2, acumulado)
                print(resultado)
                print(
                    f'As cartas acumuladas são: {acumulado}\nVamos continuar na mesma rodada, pegando novas cartas. Quem ganhar, leva todas!')
                input("Aperte ENTER para continuar")

                if verificarOponenteCampeao(jogador_2):
                    print(
                        f'Acabou o jogo! {jogador_1.nome} ganhou, pois o {jogador_2.nome} não possui mais cartas depois desse empate.')
                    break
                elif verificarOponenteCampeao(jogador_2) is False:
                    for carta in jogador_1.cartas_acumuladas:
                        jogador_1.cartas.empilha(carta)
                        jogador_1.cartas_acumuladas.pop(0)

                if verificarOponenteCampeao(jogador_1):
                    print(
                        f'Acabou o jogo! {jogador_2.nome} ganhou, pois o {jogador_1.nome} não possui mais cartas depois desse empate.')
                    break
                elif verificarOponenteCampeao(jogador_2) is False:
                    for carta in jogador_1.cartas_acumuladas:
                        jogador_1.cartas.empilha(carta)
                        jogador_1.cartas_acumuladas.pop(0)

                carta_j1 = jogador_1.retiraCarta()
                carta_j2 = jogador_2.retiraCarta()
                print(f'\nA carta de {jogador_1.nome} é: {carta_j1}\nA carta de {jogador_2.nome} é: {carta_j2}')

            resultado, acumulado, jogadas1, jogadas2 = compararCartas(carta_j1, carta_j2, acumulado)

            if jogadas1 == "perdeu":
                for lista in jogadas2:
                    jogador_2.pegarCartaOponente(lista)
                print(f'{jogador_1.nome} perdeu a rodada {rodada}')
            if jogadas2 == "perdeu":
                for lista in jogadas1:
                    jogador_1.pegarCartaOponente(lista)
                print(f'{jogador_2.nome} perdeu a rodada {rodada}')
            print(
                f'{jogador_1.nome} possui {jogador_1.quantificarCartas()} cartas e {jogador_2.nome} possui {jogador_2.quantificarCartas()} cartas!')
            if verificarOponenteCampeao(jogador_2):
                print(f'Fim do jogo. O {jogador_1.nome} venceu o jogo')
                break
            elif verificarOponenteCampeao(jogador_2) is False:
                for carta in jogador_1.cartas_acumuladas:
                    jogador_1.cartas.empilha(carta)
                    jogador_1.cartas_acumuladas.pop(0)
            elif verificarOponenteCampeao(jogador_1):
                print(f'Fim do jogo. O {jogador_2.nome} venceu o jogo')
                break
            elif verificarOponenteCampeao(jogador_2) is False:
                for carta in jogador_1.cartas_acumuladas:
                    jogador_1.cartas.empilha(carta)
                    jogador_1.cartas_acumuladas.pop(0)
            else:
                if rodada >= rodada_fim:

                    if jogador_1.quantificarCartas() > jogador_2.quantificarCartas():
                        print(f'{jogador_1.nome} é o ganhador!')
                        while novo_jogo != 'S' and novo_jogo != 'N':
                            try:
                                novo_jogo = input('Deseja jogar novamente? Valores Válidos: [S/N]').strip()[0]
                            except IndexError:
                                print('ERRO: informe um valor válido [S/N]')
                            except KeyboardInterrupt:
                                print('Leitura de dados interrompida pelo usuário')
                        if novo_jogo.upper() == 'N':
                            print('Até a próxima!')
                            exit()
                        else:
                            rodada_fim = 0
                            while confirma_troca_nome != 'S' and confirma_troca_nome != 'N':
                                try:
                                    confirma_troca_nome = input('Trocar nomes? [S/N]').strip()[0].upper()
                                except IndexError:
                                    print('ERRO: informe um valor válido [S/N]')
                                except KeyboardInterrupt:
                                    print('Leitura de dados interrompida pelo usuário')
                            if confirma_troca_nome == 'S':
                                trocar_nome = True
                                break
                            elif confirma_troca_nome == 'N':
                                trocar_nome = False
                                break
                    elif jogador_1.quantificarCartas() < jogador_2.quantificarCartas():
                        print(f'{jogador_2.nome} é o ganhador!')
                        while novo_jogo != 'S' and novo_jogo != 'N':
                            try:
                                novo_jogo = input('Deseja jogar novamente? Valores Válidos: [S/N]').strip()[0]
                            except IndexError:
                                print('ERRO: informe um valor válido [S/N]')
                            except KeyboardInterrupt:
                                print('Leitura de dados interrompida pelo usuário')
                        if novo_jogo.upper() == 'N':
                            print('Até a próxima!')
                            exit()
                        else:
                            rodada_fim = 0
                            while confirma_troca_nome != 'S' and confirma_troca_nome != 'N':
                                try:
                                    confirma_troca_nome = input('Trocar nomes? Valores Válidos: [S/N]').strip()[
                                        0].upper()
                                except IndexError:
                                    print('ERRO: informe um valor válido [S/N]')
                                except KeyboardInterrupt:
                                    print('Leitura de dados interrompida pelo usuário')
                            if confirma_troca_nome == 'S':
                                trocar_nome = True
                                break
                            elif confirma_troca_nome == 'N':
                                trocar_nome = False
                                break

                    else:
                        print('Empate na quantidade de cartas dos jogadores.\n\nAgora é a decisiva!!!')
                print("\n##########################\nVamos para mais uma rodada!\n##########################")
                input("Aperte ENTER para continuar")
                limpar_tela()


if __name__ == '__main__':
    main()
