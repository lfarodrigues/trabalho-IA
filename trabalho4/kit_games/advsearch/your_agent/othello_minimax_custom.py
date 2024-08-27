import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.

    return minimax_move(state, 4, evaluate_custom) 

def evaluate_custom(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    playerCnt = 0
    enemyCnt = 0
    board = state.get_board()
    
    for row in state.board.tiles:
        for tile in row:
            if tile == player:
                playerCnt = playerCnt + 1
            elif tile == state.board.opponent(player):
                enemyCnt = enemyCnt + 1

    points = playerCnt - enemyCnt    
    
    extra_points = [(0,0), (0,7), (7,0), (7,7)]
    for point in extra_points:
        if board.tiles[point[0]][point[1]] == player:
            points += 4

    for x in range(0, 8):
        for y in range(0, 8):
            if board.tiles[x][y] == player:
                stable = True
                for dirX, dirY in Board.DIRECTIONS:
                    px = x + dirX
                    py = y + dirY
                    if 0 <= px <= 7 and 0 <= py <= 7 and board.tiles[px][py] != player:
                        stable = False
                        break
                if stable:
                    points += 2

    if state.is_terminal():
        if state.winner() == player:
            points = 1
        elif state.winner() == state.board.opponent(player):
            points = -1
        else:
            points = 0

    return points