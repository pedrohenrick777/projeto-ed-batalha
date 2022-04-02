def comparar_cartas(carta_j1, carta_j2):
    if carta_j1.valor == carta_j2.valor:
        return 'As cartas estão empatadas'
    elif carta_j1.valor > carta_j2.valor:
        return 'O jogador 1 vence a rodada'
    else:
        return 'O jogador 2 vence a rodada'
