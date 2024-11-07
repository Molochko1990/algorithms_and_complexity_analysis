def max_wire_length(n, k, wires):
    left, right = 1, max(wires)

    def can_cut(length):
        # считаем сколько кусков получилось при текущей длине
        return sum(wire // length for wire in wires) >= k

    result = 0
    while left <= right:
        mid = (left + right) // 2
        if can_cut(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result


test_cases = [
    # (n, k,         wires,    expected_result)
    (4, 11, [802, 743, 457, 539], 200),
    (3, 10, [1000, 1000, 1000], 250),
    (5, 5, [400, 500, 600, 700, 800], 400),
    (3, 7, [300, 500, 700], 175),
    (5, 1, [100, 200, 300, 400, 500], 500),
]






for i, (n, k, wires, expected) in enumerate(test_cases):
    result = max_wire_length(n, k, wires)
    assert result == expected, f"Тест {i + 1} не прошёл: ожидается {expected}, получено {result}"
    print(f"Тест {i + 1} прошёл успешно: ожидается {expected}, получено {result}")



# общая суть получить количество кусочков (k) с максимально возможной длинной.
# используя бинарный поиск находим необходимую длинну