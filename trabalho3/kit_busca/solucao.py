from asyncio import PriorityQueue
from dataclasses import dataclass, field
import queue
from typing import Iterable, Set, Tuple

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
    
    def __str__(self) -> str:
        print('{ NODO: \'estado\' = \'' + self.estado + '\', \'pai\' = \'' + ('None' if self.pai == None else self.pai.estado) + '\', \'acao\' = \'' + self.acao + '\' }' )

@dataclass(order=True)
class NodoComPrioridade:
    priority: int
    item: Nodo=field(compare=False)

class MyPriorityQueue(queue.PriorityQueue):
    def __init__(self, heuristica):
        super().__init__()
        self.heuristica = heuristica

    def put(self, val):
        super().put(NodoComPrioridade(priority=self.heuristica(val.estado) + val.custo, item = val))

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

def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # movimentos possíveis para cada estado
    right = [0, 1, 3, 4, 6, 7]
    left = [1, 2, 4, 5, 7, 8]
    up = [3, 4, 5, 6, 7, 8]
    down = [0, 1, 2, 3, 4 ,5]

    # lista resultante
    lst_tuples = set()

    # procura índice do bloco vazio
    index = estado.index('_')    
    if index in right:
        new_state = change_char_pos(estado, index, index+1)
        lst_tuples.add(('direita', new_state))
    if index in left:
        new_state = change_char_pos(estado, index, index-1)
        lst_tuples.add(('esquerda', new_state))
    if index in up:
        new_state = change_char_pos(estado, index, index-3)
        lst_tuples.add(('acima', new_state))
    if index in down:
        new_state = change_char_pos(estado, index, index+3)
        lst_tuples.add(('abaixo', new_state))

    return lst_tuples

def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    lst_nodos = set()
    lst_filhos = sucessor(nodo.estado)

    if lst_filhos is not None:
        for f in lst_filhos:
            acao = f[0]
            estado = f[1]
            novo_nodo = Nodo(estado, nodo, acao, nodo.custo + 1)
            lst_nodos.add(novo_nodo)

    return lst_nodos

def busca_grafo(s, objetivo):
    if not possui_solucao(s): 
        return None
    X = set()
    F = objetivo()
    F.put(Nodo(s, None, None, 0))

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

def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return busca_grafo(estado, lambda: MyPriorityQueue(hamming_distance))

def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return busca_grafo(estado, lambda: MyPriorityQueue(manhattan_distance))

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return busca_grafo(estado, queue.Queue)

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return busca_grafo(estado, queue.LifoQueue)

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

# Soma do numero de caracteres na posicao correta
def hamming_distance(estado):
    return sum(char1 != char2 for char1, char2 in zip("12345678", estado))

# Distancia entre a posicao atual e a correta
posicoes = {"1":(0,0),"2":(0,1),"3":(0,2),"4":(1,0),"5":(1,1),"6":(1,2),"7":(2,0),"8":(2,1)}

def manhattan_distance(estado):
    caracteres = ["1","2","3","4","5","6","7","8"]
    
    def obter_coordenada_caractere(caractere):
        indice = estado.find(caractere)
        coluna = indice % 3
        linha = indice // 3
        return linha, coluna
    
    distancia = 0
    for c in caracteres:
        linha, coluna = obter_coordenada_caractere(c)
        valor = posicoes[c]
        distancia += abs(linha - valor[0]) + abs(coluna - valor[1])
    
    return distancia