class RodadaFimException(Exception):
    """Classe para excessão de fim de jogo, utilizada quando a partida tiver uma rodada fim e esta for alcançada"""

    def __init__(self):
        """ Construtor padrão que inicializa a classe de exceção da rodada"""
        super().__init__()
