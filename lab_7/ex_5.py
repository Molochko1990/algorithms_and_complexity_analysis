def count_rugs(matrix, N, M):
    def dfs(x, y):
        if x < 0 or x >= N or y < 0 or y >= M or matrix[x][y] != '+':
            return
        # Помечаем текущую клетку как посещённую, заменяя '+' на '.'
        matrix[x][y] = '.'
        # Рекурсивно вызываем dfs для всех восьми направлений
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x - 1, y - 1)

    rug_count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '+':
                # Когда находим закрашенную клетку, запускаем DFS
                dfs(i, j)
                # Увеличиваем счётчик ковриков
                rug_count += 1

    return rug_count

# Пример использования
if __name__ == "__main__":
    # Входные данные
    N, M = 6, 6
    matrix = [
        ".++++.",
        ".....+",
        "+..+..",
        "..++..",
        ".+....",
        ".+...+"
    ]

    # Преобразуем строки в список списков для удобства работы
    matrix = [list(row) for row in matrix]

    # Подсчитываем количество ковриков
    result = count_rugs(matrix, N, M)
    print(f"Количество ковриков: {result}")
