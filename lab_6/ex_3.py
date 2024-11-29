import unittest


def minimal_points_after_dance(L, N, points):
    points.sort()  # Сортируем координаты точек
    merged_count = 0  # Считаем количество "групп" точек
    current_range_end = -float('inf')  # Конец текущего диапазона

    for point in points:
        if point - L > current_range_end:
            # Если точка не попадает в текущий диапазон, начинаем новую группу
            merged_count += 1
            current_range_end = point + L  # Обновляем конец диапазона

    return merged_count


class TestMinimalPointsAfterDance(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minimal_points_after_dance(10, 5, [30, 3, 14, 19, 21]), 2)

    def test_case_2(self):
        self.assertEqual(minimal_points_after_dance(5, 4, [1, 6, 11, 16]), 2)

    def test_case_3(self):
        self.assertEqual(minimal_points_after_dance(2, 6, [1, 2, 4, 5, 7, 8]), 2)

    def test_case_4(self):
        self.assertEqual(minimal_points_after_dance(0, 3, [1, 2, 3]), 3)

    def test_case_5(self):
        self.assertEqual(minimal_points_after_dance(100, 3, [-50, 0, 50]), 1)

    def test_case_6(self):
        self.assertEqual(minimal_points_after_dance(1, 7, [1, 2, 4, 5, 7, 8, 10]), 4)

    def test_case_7(self):
        self.assertEqual(minimal_points_after_dance(50, 5, [-100, -50, 0, 50, 100]), 2)

    def test_case_8(self):
        self.assertEqual(minimal_points_after_dance(10, 8, [0, 10, 20, 30, 15, 25, 5, 35]), 2)

    def test_case_9(self):
        self.assertEqual(minimal_points_after_dance(15, 10, [-100, -80, -60, -40, -20, 0, 20, 40, 60, 80]), 5)


# Запуск тестов
if __name__ == "__main__":
    unittest.main()

