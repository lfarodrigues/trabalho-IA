import random
from typing import Tuple
from ..tttm.gamestate import GameState
from ..tttm.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax para o estado de jogo fornecido.
    :param state: estado para fazer a jogada
    :return: tupla (int, int) com as coordenadas x, y da jogada (lembre-se: 0 é a primeira linha/coluna)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada do Jogo da Tic-Tac-Toe Misere
    # Remova-o e coloque uma chamada para o minimax_move com 
    # a sua implementacao da poda alpha-beta. Use profundidade ilimitada na sua entrega,
    # uma vez que o jogo tem profundidade maxima 9. 
    # Preencha a funcao utility com o valor de um estado terminal e passe-a como funcao de avaliação para seu minimax_move
    legal_moves = list(state.legal_moves())
    print("\nPermitidos:",legal_moves,"\n")

    tabuleiro=state.get_board().board
    print("tabuleiro:",tabuleiro)

    jogada= melhor_jogada(tabuleiro)
    print("Jogada:",jogada)

    return jogada


   # return random.choice(legal_moves) if len(legal_moves) > 0 else (-1, -1)
   # return random.choice(range(3)), random.choice(range(3))

def utility(state, player:str) -> float:
    """
    Retorna a utilidade de um estado (terminal) 
    """
    return 0   # substitua pelo seu codigo


#--------------------------------
def melhor_jogada(tabuleiro):
    """
    Encontra a melhor jogada usando minimax com poda alfa-beta para Tic-Tac-Toe Misere.
    
    :param tabuleiro: lista de listas representando o tabuleiro do jogo, com 'W', 'B' ou vazio ('.').
    :param simbolo_jogador: símbolo do jogador atual ('W' ou 'B').
    :return: tupla (linha, coluna) da melhor jogada.
    """

    print("Jogadas válidas:",jogadas_validas(tabuleiro))
    simbolo_jogador='B'

    def minimax(tab, profundidade, alfa, beta, maximizando, simbolo_jogador):
        oponente = 'W'
        simbolo_jogador = 'B'

        vencedor = verifica_vencedor(tab)
        
        if vencedor == simbolo_jogador:
            return -1  # Perder é ruim, então retorna valor negativo
        elif vencedor == oponente:
            return 1  # Se o oponente perde, isso é bom
        elif not movimentos_restantes(tab):
            return 0  # Empate

        if maximizando:
            max_eval = float('-inf')
            for linha, coluna in jogadas_validas(tab):
                tab[linha][coluna] = simbolo_jogador
                eval = minimax(tab, profundidade + 1, alfa, beta, False, simbolo_jogador)
                tab[linha][coluna] = '.'
                max_eval = max(max_eval, eval)
                alfa = max(alfa, eval)
                if beta <= alfa:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for linha, coluna in jogadas_validas(tab):
                tab[linha][coluna] = oponente
                eval = minimax(tab, profundidade + 1, alfa, beta, True, simbolo_jogador)
                tab[linha][coluna] = '.'
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alfa:
                    break
            return min_eval

    melhor_valor = -float('inf')
    melhor_movimento = None
    for coluna, linha in jogadas_validas(tabuleiro):
        tabuleiro[linha][coluna] = simbolo_jogador
        movimento_valor = minimax(tabuleiro, 0, -float('inf'), float('inf'), False, simbolo_jogador)
        tabuleiro[linha][coluna] = '.'
        if movimento_valor > melhor_valor:
            melhor_valor = movimento_valor
            melhor_movimento = (linha, coluna)
    
    return melhor_movimento

def jogadas_validas(tab):
    """Retorna uma lista de coordenadas (linha, coluna) para movimentos válidos no tabuleiro."""
    return [(i, j) for i in range(3) for j in range(3) if tab[i][j] == '.']

def movimentos_restantes(tab):
    """Verifica se ainda há movimentos restantes no tabuleiro."""
    return any(tab[i][j] == '.' for i in range(3) for j in range(3))

def verifica_vencedor(tab):
    """Verifica se há um vencedor no tabuleiro."""
    linhas = [row for row in tab]
    colunas = [[tab[j][i] for j in range(3)] for i in range(3)]
    diagonais = [[tab[i][i] for i in range(3)], [tab[i][2-i] for i in range(3)]]
    
    for linha in linhas + colunas + diagonais:
        if linha[0] == linha[1] == linha[2] != '.':
            return linha[0]
    return None

# Exemplo de uso
# tabuleiro_exemplo = [
#     ['B', 'W', 'B'],
#     ['W', 'B', '.'],
#     ['.', '.', 'W']
# ]
# simbolo_jogador = 'W'
# print(melhor_jogada(tabuleiro_exemplo, simbolo_jogador))

