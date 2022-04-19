import os


class Tela:
    """Classe criada para limpar a tela"""

    def limpar_tela():
        """Método criado para limpar a tela"""
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
