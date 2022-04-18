from core.Baralho import *
from core.Jogador import *
from utils.JogoExceptions import *
from utils.Tela import Tela

if __name__ == '__main__':
    trocar_nome = True
    cartas_acumuladas = []

    while True:
        rodada = 1
        try:
            Tela.limpar_tela()
            if trocar_nome:
                nome_j1 = input('Nome do Jogador 1: ')
                nome_j2 = input('Nome do Jogador 2: ')
            jogador_1 = Jogador(nome_j1)
            jogador_2 = Jogador(nome_j2)
            rodada_fim = int(input('Digite a quantidade de rodadas (vazio para o jogo terminar quando um dos jogadores não tiver mais cartas): '))
        except NomeJogadorException:
            print('É preciso digitar o(s) nome(s) do(s) jogador(es). ENTER para continuar')
            input()
            continue
        except ValueError:
            rodada_fim = None

        baralho = Baralho()
        cont = 0
        while True:
            try:
                if cont % 2 == 0:
                    jogador_1.receberCartas(baralho.retirarCarta())
                else:
                    jogador_2.receberCartas(baralho.retirarCarta())
                cont += 1
            except BaralhoVazioException:
                break
        Tela.limpar_tela()
        input('Vamos começar. ENTER para continuar')
        while True:
            try:
                Tela.limpar_tela()
                print('#'*5 + f' Rodada {rodada} ' + '#'*5 + '\n')
                print(f'{jogador_1} tem {jogador_1.numeroCartas} cartas.')
                print(f'{jogador_2} tem {jogador_2.numeroCartas} cartas.\n')
                carta_j1 = jogador_1.retiraCarta()
                carta_j2 = jogador_2.retiraCarta()
                print((f'Carta de {jogador_1}: {carta_j1}'),
                    (f'Carta de {jogador_2}: {carta_j2}'), sep='\n')
                if carta_j1.valor == carta_j2.valor:
                    print('\nCartas Empatadas, Vamos á rodada desempate!')
                    cartas_acumuladas.append(carta_j1)
                    cartas_acumuladas.append(carta_j2)
                elif carta_j1.valor > carta_j2.valor:
                    print(f'\n{jogador_1} é o vencedor')
                    while len(cartas_acumuladas) != 0:
                        carta = cartas_acumuladas.pop()
                        jogador_1.pegarCartaOponente(carta)
                    jogador_1.pegarCartaOponente(carta_j1)
                    jogador_1.pegarCartaOponente(carta_j2)
                else:
                    print(f'\n{jogador_2} é o vencedor')
                    while len(cartas_acumuladas) != 0:
                        carta = cartas_acumuladas.pop()
                        jogador_2.pegarCartaOponente(carta)
                    jogador_2.pegarCartaOponente(carta_j1)
                    jogador_2.pegarCartaOponente(carta_j2)
                
                input('\n\rENTER para continuar.')
                if rodada_fim is not None:
                    if rodada_fim <= rodada:
                        raise RodadaFimException
                rodada+=1
            except RodadaFimException:
                if jogador_1.numeroCartas == jogador_2.numeroCartas:
                    print('Os jogadores tem a mesma quantidade de cartas, vamos a uma rodada desempate!')
                    input('\rENTER para continuar.')
                    rodada += 1
                    continue
                print('\nFim de Partida!')
                if jogador_1.numeroCartas > jogador_2.numeroCartas:
                    print(f'{jogador_1} vence a partida!')
                else:
                    print(f'{jogador_1} vence a partida!')

                break
            except JogadorSemCartasException:
                if jogador_1.numeroCartas == 0:
                    print(f'{jogador_2} vence a partida')
                else:
                    print(f'{jogador_1} vence a partida')
                input('ENTER para continuar')
                break
        Tela.limpar_tela()
        novo_jogo = input('Novo jogo? [S/N]').upper()
        if not novo_jogo == 'S':
            exit()

        trocar_nome = True if input('Trocar nomes? [S/N]').upper() == 'S' else False


