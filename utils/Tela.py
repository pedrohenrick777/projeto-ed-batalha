import os


class Tela:
    def limpar_tela():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
