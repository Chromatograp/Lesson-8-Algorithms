from typing import List

print('Задание 1.')


# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

friends = int(input('Введите количество друзей: '))

count = 0
matrix = []
while count < friends:
    matrix.append([1] * friends)
    count += 1
    for i in matrix:
        i[0 + matrix.index(i)] = 0
print('Количество всех возможных рукопожатий:', (sum(sum(i) for i in matrix)) / 2)