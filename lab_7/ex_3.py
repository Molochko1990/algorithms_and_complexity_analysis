from collections import deque


def can_measure(N, M, K, L):
    if L > N:
        return "OOPS"

    # Создаем очередь для BFS
    queue = deque([(N, 0, 0)])  # Начальное состояние
    visited = set(queue)

    # BFS
    steps = 0
    while queue:
        # Проходим по всем состояниям текущего уровня
        for _ in range(len(queue)):
            x, y, z = queue.popleft()

            # Проверяем, достигли ли мы нужного состояния
            if x == L:
                return steps

            # Генерируем все возможные новые состояния
            # Переливания между колбами
            new_states = [
                (0, y + x, z) if y + x <= M else (x - (M - y), M, z),
                (0, y, z + x) if z + x <= K else (x - (K - z), y, K),
                (x + y, 0, z) if x + y <= N else (N, y - (N - x), z),
                (x, 0, z + y) if z + y <= K else (x, y - (K - z), K),
                (x + z, y, 0) if x + z <= N else (N, y, z - (N - x)),
                (x, y + z, 0) if y + z <= M else (x, M, z - (M - y))
            ]

            # Добавляем новые состояния в очередь
            for state in new_states:
                if state not in visited:
                    visited.add(state)
                    queue.append(state)

        # Увеличиваем количество шагов
        steps += 1

    # Если вышли из цикла и не нашли решение
    return "OOPS"


# Пример использования
N, M, K, L = 5, 3, 2, 4
print(can_measure(N, M, K, L))  # Выводит количество необходимых переливаний или "OOPS"
