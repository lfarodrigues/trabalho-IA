import random
from typing import Tuple, Callable



def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    _, best_move = minimax(state, max_depth, float('-inf'), float('inf'), state.player == 'B', eval_func)
    return best_move

def minimax(state, depth, alpha, beta, max_player, eval_func:Callable):
    if state.is_terminal() or depth == 0:
        return eval_func(state, state), None
    
    best_move = None

    if max_player:
        best_value = float('-inf')
        for move in state.legal_moves():
            next_state = state.next_state(move)
            value, _ = minimax(next_state, depth-1, alpha, beta, False, eval_func)
            
            if value > best_value:
                best_value = value
                best_move = move
            
            alpha = max(alpha, best_value)
            
            if beta <= alpha:
                break
        return best_value, best_move
    else:
        best_value = float('inf')
        for move in state.legal_moves():
            next_state = state.next_state(move)
            value, _ = minimax(next_state, depth - 1, alpha, beta, True, eval_func)
            if value < best_value:
                best_value = value
                best_move = move
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value, best_move
