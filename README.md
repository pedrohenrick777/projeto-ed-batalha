# 📋 Projeto - Baralho

### 1. O Problema

Considere o exercício da modelagem e codificação de um baralho tradicional de 52 cartas estudado em sala de aula (código disponibilizado à esta atividade). Neste exercício, você deverá implementar um jogo simples que utiliza as cartas de um baralho chamado “Batalha”.

O jogo “Batalha” é bem simples: divide-se as cartas do baralho, igualmente, para dois jogadores. A menor carta é o Ás e a maior do baralho é o Rei. Não importa o naipe. Cada jogador inicia com seu próprio conjunto de cartas empilhadas, viradas para baixo. A batalha começa quando cada jogador retira uma carta do topo do seu baralho e a revela na mesa. Então, aquele que apresentar a carta de maior valor, vence a batalha e recebe a carta do outro jogador. As duas cartas são adicionadas à base do baralho. 

No caso de cada jogador apresentar a mesma carta, elas ficam bloqueadas e outro par de cartas é puxado. Ganha o total de cartas acumuladas o jogador que desempatar a batalha.

### 2. Simulação

Para fins de correção, a equipe deve exibir uma interface que apresente o passo-a-passo das batalhas (com pausa entre as jogadas para se ter maior controle) e permita acompanhar o que está acontecendo em cada jogada. A simulação mais clara e precisa alcançará a pontuação máxima definida para esse critério de correção.

### 3. Requisitos Funcionais

A implementação desta atividade de avaliação deve levar em conta o atendimento aos seguintes requisitos funcionais:


●	Iniciar o jogo definindo os jogadores e sua mão de cartas.  As cartas devem estar embaralhadas antes da distribuição. [10 pontos]

●	Simulação: acompanhamento da saída de cada batalha. A clareza de informações exibidas na tela é importante para a avaliação. Sugestão: informar o número de ordem da batalha, quem ganhou e o total de cartas atualizada de cada jogador, considerando já as cartas que recebeu do adversário. [30 pontos]

●	No caso de empate, mostrar na tela as jogadas subsequentes e a retenção das cartas até que haja um vencedor. [20 pontos]

●	Permitir que ao término do jogo, o usuário decida se quer jogar novamente ou encerrar o programa. Se for jogar novamente [20 pontos]


### 4. Requisitos não-funcionais

A implementação deste projeto deve levar em conta o atendimento aos seguintes requisitos não-funcionais:


●	Modelar a classe Jogador para o problema em questão, utilizando os princípios OO. [20 pontos]

●	Utilizar exclusivamente o código do baralho disponibilizado para esta atividade. Ao Baralho, substitua a coleção de cartas por uma pilha também disponibilizada junto com esta atividade. Só será usado 1 Baralho. Não serão corrigidas soluções que não apliquem a Pilha.

●	Modularização;

●	Encapsulamento;

●	Tratamento de exceções;

●	Documentação do código;

●	Facilidade de utilização do programa;

●	Interação programa/usuário na exibição das mensagens do sistema (de erro ou de orientação);

●	Apresentação de dados de forma organizada, na tela;


O não atendimento a estes requisitos não-funcionais implicará em um redutor na nota.

### 5. Informações Importantes
 Uma má estrutura do programa, logo no início, prejudicará potencialmente o desenvolvimento do código. Contate o monitor ou professor para direcionar adequadamente a codificação do seu projeto. Não haverá a menor possibilidade do aluno não ter assistência para desenvolver o projeto. Lógica e/ou operações copiadas serão anuladas em todas as cópias, independente de quem fez e quem copiou.
