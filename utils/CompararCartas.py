def compararCartas(carta_j1, carta_j2, acumulado):

    if carta_j1.valor == carta_j2.valor:
        resultado = 'As cartas estão empatadas'
        acumulado.append(carta_j1)
        acumulado.append(carta_j2)
        jogadas1 = []
        jogadas2 = []
        return resultado, acumulado, jogadas1, jogadas2

    elif carta_j1.valor > carta_j2.valor:
        resultado = 'O jogador 1 vence a rodada'
        lista_jogador1 = list(acumulado)
        lista_jogador1.append(carta_j2)
        lista_jogador1.append(carta_j1)
        lista_jogador2 = "perdeu"
    else:
        resultado = 'O jogador 2 vence a rodada'
        lista_jogador2 = list(acumulado)
        lista_jogador2.append(carta_j1)
        lista_jogador2.append(carta_j2)
        lista_jogador1 = "perdeu"

    return resultado, acumulado, lista_jogador1, lista_jogador2

def verificarEmpate(valor1, valor2):
    return valor1 == valor2