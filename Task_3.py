from collections import deque

print('Задание 3.')


# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины
# связаны, по алгоритму поиска в глубину (Depth-First Search).

graph = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
]

ex = set()


def dfs(node):

    ex.add(node)
    for coherence in range(len(graph)):
        if graph[node][coherence] == 1 and coherence not in ex:
            print(coherence)
            dfs(coherence)


print(dfs(0))