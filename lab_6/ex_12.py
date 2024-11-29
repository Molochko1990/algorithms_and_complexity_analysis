def can_partition(n, points):
    total_sum = sum(points)

    # Если сумма нечетная, то невозможно разбить на две равные части
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    # Инициализация dp массива
    dp = [False] * (target + 1)
    dp[0] = True

    # Заполнение dp массива
    for point in points:
        for j in range(target, point - 1, -1):
            dp[j] = dp[j] or dp[j - point]

    return dp[target]


# Пример использования
n = 3
points = [2, 10, 9]
print(can_partition(n, points))  # Вывод: True
