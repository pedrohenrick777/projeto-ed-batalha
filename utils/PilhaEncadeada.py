class PilhaException(Exception):
    """ Classe criada para retornar mensagens de exceções relacionada à Pilha Encadeada """

    def __init__(self, mensagem, metodo=''):
        """ Construtor padrão que inicializa a classe de exceção da pilha"""
        super().__init__(mensagem)
        self.metodo = metodo


class Node:
    """ Classe criada para representar o nó necessário em uma Pilha Encadeada que ajuda a guardar a ordem das cartas

        Atributos
        _________
        dado:
            atributo que considera o último valor a ser empilhado
        prox:
            atributo que guarda o valor de um 'dado' anterior, no momento que um novo dado é empilhado

        """

    def __init__(self, dado):
        """ construtor padrão que inicializa o objeto Node """
        self.dado = dado
        self.prox = None

    def insereProximo(self, dado):
        """ Método que insere o penúltimo dado recebido como o próximo valor da pilha encadada"""
        if (self.prox == None):
            self.prox = Node(dado)

    def getProximo(self):
        """ Método que retorna a representação de string do objeto Node"""
        return self.prox

    def __str__(self):
        """ Método que retorna a representação de string do objeto Node"""
        return str(self.data)

    def temProximo(self):
        """ Método que verifica se existe dado como o próximo valor da pilha  """
        return self.prox != None


class Pilha:
    """ Classe criada para representar a Pilha encadeada

    Atributos
    _________
    head:
        atributo que recebe o último objeto Node criado
    tamanho:
        atributo que armazena o tamanho atualizado da pilha encadeada

    """

    def __init__(self):
        """ construtor padrão que inicializa o objeto Baralho"""
        self.__head = None
        self.__tamanho = 0

    def estaVazia(self):
        """ Método que verifica se a pilha está vazia """
        return self.__head == None

    def tamanho(self):
        """ Método que retorna o tamanho da pilha """
        return self.__tamanho

    def elemento(self, posicao):
        """ Método que retorna o elemento na posição desejada """
        try:
            assert posicao > 0 and posicao <= self.__tamanho

            cursor = self.__head
            contador = 1
            while (cursor != None and contador < posicao):
                contador += 1
                cursor = cursor.prox

            return cursor.dado

        except TypeError:
            raise PilhaException('Digite um número inteiro referente ao elemento desejado')
        except AssertionError:
            raise PilhaException(f'O elemento {posicao} NAO existe na pilha de tamanho {self.__tamanho}')
        except:
            raise

    def busca(self, valor):
        """ Método que busca a posição do elemento desejado """
        cursor = self.__head
        contador = 1

        while (cursor != None):
            if cursor.dado == valor:
                return contador
            cursor = cursor.prox
            contador += 1

        raise PilhaException(f'Valor {valor} nao esta na pilha', 'busca()')

    def empilha(self, valor):
        """ Método que empilha os dados da Pilha"""
        novo = Node(valor)
        novo.prox = self.__head
        self.__head = novo
        self.__tamanho += 1

    def desempilha(self):
        """ Método que desempilha os dados da Pilha"""
        if not self.estaVazia():
            dado = self.__head.dado
            self.__head = self.__head.prox
            self.__tamanho -= 1
            return dado
        raise PilhaException('A pilha está vazia')

    def imprime(self):
        """ Método que imprime a representação de string do objeto Pilha"""
        print(self.__str__())

    def topo(self):
        """ Método que retorna o dado que encontra-se no topo da pilha"""
        return self.__head

    def __str__(self):
        """ Método que retorna a representação de string do objeto Pilha"""
        cursor = self.__head
        primeiro = True
        s = 'topo->['
        while (cursor != None):
            if primeiro:
                s += f'{cursor.dado}'
                primeiro = False
            else:
                s += f', {cursor.dado}'
            cursor = cursor.prox

        s += ']'
        return s
