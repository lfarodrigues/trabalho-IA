Luis Filipe Antunes Rodrigues (314848) Tiago Elias Steinke

Resultados:

a) Para o Tic-Tac-Toe misere, relate se o desempenho da sua implementação do minimax com poda alfa-beta: embora não seja simples provar que o jogo está sendo jogado com perfeição, avalie as evidências: (i) O minimax sempre ganha do randomplayer? Não, de 10 jogos, 2 vitórias, 3 empates, 5 derrotas.

(ii) O minimax sempre empata consigo mesmo? Sim, de 10 jogos, todos deu empate.

(iii) O minimax não perde para você, quando você usa a sua melhor estratégia? Depois de achar uma sequência que eu ganho, sempre ganho se seguir mesma sequência.

b) Othello

Sobre a heurística customizada: considera pontos extras para peças nos cantos e também o quão estáveis elas são

(44) Contagem de peças X Valor posicional (20)
(18) Valor posicional X Contagem de peças (46)
(35) Contagem de peças X Heurística customizada (20)
(32) Heurística customizada X Contagem de peças (32)
(23) Valor posicional X Heurística customizada (41)
(46) Heurística customizada X Valor posicional (18)

(ii) Observe e relate qual implementação foi a mais bem-sucedida.
    Em 8 de 9 vezes o jogador que iniciou jogando venceu. No confronto custom x mask, a heurística mask sendo o segundo a jogar.

(iii) Reflita sobre o que pode ter tornado cada heurística melhor ou pior, em termos de performance.
    O mask considere número de peças no tabuleiro e dá pontos para suas posições. Aparenta ter a melhor performance.

