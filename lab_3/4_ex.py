from lab_3.ex_1 import Deque


class MinQueue:
    def __init__(self):
        self.main_queue = Deque(10000)
        self.min_queue = Deque(10000)

    def push(self, value):
        self.main_queue.push_back(value)

        while self.min_queue.size > 0 and self.min_queue.buffer[self.min_queue.tail - 1] > value:
            self.min_queue.pop_back()
        self.min_queue.push_back(value)

    def pop(self):
        if self.main_queue.size > 0:
            removed_element = self.main_queue.buffer[self.main_queue.head]
            self.main_queue.pop_front()
            if removed_element == self.min_queue.buffer[self.min_queue.head]:
                self.min_queue.pop_front()

    def get_min(self):
        if self.min_queue.size > 0:
            return self.min_queue.buffer[self.min_queue.head]

test_cases = [
    (["+ 10", "+ 5", "?", "-", "?", "-"], [5, 5]),
    (["+ 3", "+ 4", "+ 2", "?", "-", "?", "-", "?"], [2, 2, 2]),
    (["+ 1", "+ 1", "+ 1", "?", "-", "?", "-", "?"], [1, 1, 1]),
    (["+ 1000000000", "+ -1000000000", "?", "-", "?"], [-1000000000, -1000000000]),
    (["+ -5", "+ 0", "+ -10", "+ 15", "?", "-", "?", "-"], [-10, -10]),
    (["+ 50", "+ 40", "+ 30", "+ 20", "+ 10", "?", "-", "?", "-", "?", "-", "?", "-"], [10, 10, 10, 10]),
    (["+ 1", "?", "-"], [1]),
    (["+ 999999999", "+ 999999999", "?", "-", "?"], [999999999, 999999999]),
    (["+ 500", "+ -500", "+ 1000", "+ -1000", "?", "-", "?", "-", "?"], [-1000, -1000, -1000]),
    (["+ 1", "+ 2", "+ 3", "+ 4", "+ 5", "?", "?", "-", "?", "-", "?", "-", "?", "-", "?", "-"],
     [1, 1, 2, 3, 4, 5]),
    (["+ 10", "+ 9", "+ 8", "+ 7", "+ 6", "+ 5", "+ 4", "+ 3", "+ 2", "+ 1", "?", "-", "?", "-", "?", "-", "?", "-"],
     [1, 1, 1, 1]),
    (["+ 1000000", "+ 999999", "+ 999998", "?", "-", "?", "-", "?", "-"],
     [999998, 999998, 999998]),
    (["+ 100", "+ 200", "+ 300", "+ 50", "+ 25", "+ 10", "?", "-", "?", "-", "?", "-", "?", "-"],
     [10, 10, 10, 10]),
    (["+ 1000000000", "+ -1000000000", "+ 500", "+ -500", "+ 300", "+ -300", "?", "-", "?", "-", "?", "-", "?", "-", "?", "-"],
     [-1000000000, -1000000000, -500, -500, -300]),
    (["+ 5", "+ 5", "+ 5", "+ 5", "+ 5", "?", "-", "?", "-", "?", "-", "?", "-"],
     [5, 5, 5, 5]),
    (["+ 1000"] * 1000 + ["?"] * 500 + ["-"] * 500 + ["?"] * 500,
     [1000] * 1000),
    (["+ -1", "+ -2", "+ -3", "+ -4", "+ -5", "?", "-", "?", "-", "?", "-", "?", "-"],
     [-5, -5, -5, -5])
]

for i, (commands, expected_output) in enumerate(test_cases):
    queue = MinQueue()
    results = []

    for command in commands:
        if command.startswith('+'):
            _, value = command.split()
            queue.push(int(value))

        elif command == '-':
            queue.pop()

        elif command == '?':
            results.append(queue.get_min())

    print(f"Тест {i + 1}:")
    print(f"Команды: {commands}")
    print(f"Ожидаемый результат: {expected_output}")
    print(f"Полученный результат: {results}")
    print(f"Тест пройден: {results == expected_output}\n")
