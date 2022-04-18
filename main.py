from core.Baralho import *
from core.Jogador import *
from utils.JogoExceptions import *
from utils.Tela import Tela

if __name__ == '__main__':
    trocar_nome = True  # variável utilizada para verificar a necessidade de trocar o nome dos jogadores. Se for true, novos nomes serão solicitados.
    cartas_acumuladas = []  # lista para armazenar as cartas acumuladas pelos jogadores

    while True:
        rodada = 1  # variável que representa as rodadas
        try:
            Tela.limpar_tela()
            if trocar_nome:
                nome_j1 = input('Nome do Jogador 1: ')
                nome_j2 = input('Nome do Jogador 2: ')
            jogador_1 = Jogador(nome_j1)  # instanciando o Objeto Jogador para o primeiro jogador
            jogador_2 = Jogador(nome_j2)  # instanciando o Objeto Jogador para o segundo jogador
            while True:
                try:
                    Tela.limpar_tela()
                    rodada_fim = int(input(
                        'Digite a quantidade de rodadas (vazio para o jogo terminar quando um dos jogadores não tiver mais cartas): '))  # variável para pegar a quantidade de rodadas desejadas
                    assert rodada_fim > 0
                    break
                except AssertionError:
                    print('Digite um número maior que 0 ou deixe o campo vazio')
                    continue
                except ValueError:
                    rodada_fim = None
                    break

        except KeyboardInterrupt:
            print('Leitura de dados interrompida pelo usuário')

        except NomeJogadorException:
            print('É preciso digitar o(s) nome(s) do(s) jogador(es). ENTER para continuar')
            input()
            continue

        baralho = Baralho()  # instanciando o Objeto Baralho
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
                print('#' * 5 + f' Rodada {rodada} ' + '#' * 5 + '\n')  # imprime o número de rodadas
                print(
                    f'{jogador_1} tem {jogador_1.numeroCartas} cartas.')  # imprime a quantidade de cartas que o jogador 1 tem
                print(
                    f'{jogador_2} tem {jogador_2.numeroCartas} cartas.\n')  # imprime a quantidade de cartas que o jogador 2 tem
                carta_j1 = jogador_1.retiraCarta()  # retira a carta da vez da batalha para o jogador 1
                carta_j2 = jogador_2.retiraCarta()  # retira a carta da vez da batalha para o jogador 2
                print((f'Carta de {jogador_1}: {carta_j1}'),
                      (f'Carta de {jogador_2}: {carta_j2}'), sep='\n')
                if carta_j1.valor == carta_j2.valor:  # verifica se as cartas possuem o mesmo valor
                    print('\nCartas Empatadas, Vamos à rodada desempate!')
                    # adicionando cartas acumuladas
                    cartas_acumuladas.append(carta_j1)
                    cartas_acumuladas.append(carta_j2)
                elif carta_j1.valor > carta_j2.valor:  # verifica se a carta do jogador 1 possui um valor maior que a do jogador 2
                    print(f'\n{jogador_1} é o vencedor')
                    # pegar cartas do oponente
                    while len(cartas_acumuladas) != 0:
                        carta = cartas_acumuladas.pop()
                        jogador_1.pegarCartaOponente(carta)
                    jogador_1.pegarCartaOponente(carta_j1)
                    jogador_1.pegarCartaOponente(carta_j2)
                else:  # a carta do jogador 2 possui um valor maior que a do jogador 1
                    print(f'\n{jogador_2} é o vencedor')
                    # pegar cartas do oponente
                    while len(cartas_acumuladas) != 0:
                        carta = cartas_acumuladas.pop()
                        jogador_2.pegarCartaOponente(carta)
                    jogador_2.pegarCartaOponente(carta_j1)
                    jogador_2.pegarCartaOponente(carta_j2)

                input('\n\rENTER para continuar.')
                # verifica se chegou o momento do fim da partida
                if rodada_fim is not None:
                    if rodada_fim <= rodada:
                        raise RodadaFimException
                rodada += 1
            except RodadaFimException:
                # verifica se no fim das rodadas previstas deu empate
                if jogador_1.numeroCartas == jogador_2.numeroCartas:
                    print('Os jogadores tem a mesma quantidade de cartas, vamos a uma rodada desempate!')
                    input('\rENTER para continuar.')
                    rodada += 1
                    continue
                print('\nFim de Partida!')
                # printa quem ganhou o jogo
                if jogador_1.numeroCartas > jogador_2.numeroCartas:
                    print(f'{jogador_1} vence a partida com {jogador_1.numeroCartas} cartas!')
                else:
                    print(f'{jogador_2} vence a partida com {jogador_2.numeroCartas} cartas!')

                break
            except JogadorSemCartasException:
                if jogador_1.numeroCartas == 0:
                    print(f'{jogador_2} vence a partida com {jogador_2.numeroCartas} cartas')
                else:
                    print(f'{jogador_1} vence a partida com {jogador_2.numeroCartas} cartas')
                input('ENTER para continuar')
                break
        Tela.limpar_tela()
        novo_jogo = input(
            'Novo jogo? [S para Sim; Qualquer outro valor é ignorado]: ').upper()  # recebe a confirmação se haverá um novo jogo ou não
        if not novo_jogo == 'S':
            exit()

        trocar_nome = True if input(
            'Trocar nomes? [S para Sim; Qualquer outro valor é ignorado]').upper() == 'S' else False  # recebe a confirmação se haverá a troca de nome dos jogadores
