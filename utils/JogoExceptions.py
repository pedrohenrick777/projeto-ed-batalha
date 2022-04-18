class RodadaFimException(Exception):
    '''Excessão de fim de jogo, utilizada quando a partida tiver uma rodada fim e esta for alcançada'''
    def __init__(self):
        super().__init__()
