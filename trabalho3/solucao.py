from dataclasses import dataclass, field
from queue import PriorityQueue
import sys
class Nodo:
    def __init__(self, estado, pai, acao):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = 0 if pai == None else pai.custo + 1
    
    def __eq__(self, outro):
        if isinstance(outro, Nodo):
            return self.estado == self.estado
        return False
    
    def __hash__():
        pass
    def __str__(self) -> str:
        print('{ NODO: \'estado\' = \'' + self.estado + '\', \'pai\' = \'' + ('None' if self.pai == None else self.pai.estado) + '\', \'acao\' = \'' + self.acao + '\' }' )

@dataclass(order=True)
class NodoHeuristica:
    priority: int
    item: Nodo=field(compare=False)

class AstarPriorityQueue(PriorityQueue):
    def __init__(self, heuristica):
        super().__init__()
        self.heuristica = heuristica

    def put(self, val):
        super().put(NodoHeuristica(priority=self.heuristica(val.estado) + val.custo, item = val))

    def get(self):
        return super().get().item

def change_char_pos(string, pos1, pos2):
    # Verificar se os índices estão dentro do intervalo da string
    if pos1 < 0 or pos1 >= len(string) or pos2 < 0 or pos2 >= len(string):
        raise ValueError("Índices fora do intervalo da string")
    
    # Converter a string em uma lista de caracteres
    lst = list(string)
    
    # Trocar os caracteres nas posições pos1 e pos2
    aux = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = aux

    # Converter a lista de volta para uma string
    changed = ''.join(lst)
    
    return changed

def sucessor(estado):
    # movimentos possíveis para cada estado
    right = [0, 1, 3, 4, 6, 7]
    left = [1, 2, 4, 5, 7, 8]
    up = [3, 4, 5, 6, 7, 8]
    down = [0, 1, 2, 3, 4 ,5]

    # lista resultante
    lst_tuples = []

    # procura índice do bloco vazio
    index = estado.index('_')    
    if index in right:
        new_state = change_char_pos(estado, index, index+1)
        action_state = ('direita', new_state)
        lst_tuples.append(action_state)
    if index in left:
        new_state = change_char_pos(estado, index, index-1)
        action_state = ('esquerda', new_state)
        lst_tuples.append(action_state)
    if index in up:
        new_state = change_char_pos(estado, index, index-3)
        action_state = ('cima', new_state)
        lst_tuples.append(action_state)
    if index in down:
        new_state = change_char_pos(estado, index, index+3)
        action_state = ('baixo', new_state)
        lst_tuples.append(action_state)        

    return lst_tuples

def expande(nodo):
    lst_nodos = []
    lst_filhos = sucessor(nodo.estado)

    if lst_filhos is not None:
        for f in lst_filhos:
            acao = f[0]
            estado = f[1]
            novo_nodo = Nodo(estado, nodo, acao)
            lst_nodos.append(novo_nodo)

    return lst_nodos

def busca_grafo(s, objetivo):
    if not possui_solucao(s): return None
    X = set()
    F = objetivo()
    F.put(Nodo(s, None, ''))
    
    while not F.empty():
        V = F.get()
        if estado_objetivo(V.estado): 
            return lista_acoes(V)
        if V.estado not in X:
            X.add(V.estado)
            fronteira_V = expande(V)        
            for nodo in fronteira_V:
                F.put(nodo)
    
    return None

def estado_objetivo(estado):
    return estado == "12345678_"

def possui_solucao(s):
    lst_estados = [int(char) if char != '_' else 0 for char in s]

    inv = 0
    for i in range(9):
        for j in range(i+1,9):
            if lst_estados[j] != 0 and lst_estados[i] > lst_estados[j]:
                inv += 1

    return inv % 2 == 0

def lista_acoes(estado):
    acoes = []
    acoes.append(estado.acao)
    curr = estado.pai

    while curr is not None:
        acoes.append(curr.acao)
        curr = curr.pai

    del acoes[-1]
    acoes.reverse()
    return acoes

def astar_hamming(estado):
    return busca_grafo(estado, lambda: AstarPriorityQueue(hamming))

def hamming(estado):
    return sum(char1 != char2 for char1, char2 in zip("12345678", estado))

def astar_manhattan(estado):   
    pass

def test_astar_hamming():
    sol = astar_hamming("_12345678")
    print(sol)


test_astar_hamming()
