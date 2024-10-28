class Deque:
    def __init__(self, max_size):
        self.max_size = max_size
        self.buffer = [None] * max_size # массив который представляет собой очередь
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, value):
        if self.size == self.max_size:
            print("error")
            return
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def push_front(self, value):
        if self.size == self.max_size:
            print("error")
            return
        self.head = (self.head - 1 + self.max_size) % self.max_size
        self.buffer[self.head] = value
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            print("error")
            return
        value = self.buffer[self.head]
        print(value)
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

    def pop_back(self):
        if self.size == 0:
            print("error")
            return
        self.tail = (self.tail - 1 + self.max_size) % self.max_size
        value = self.buffer[self.tail]
        print(value)
        self.size -= 1

def process_commands(commands, max_size):
    deque = Deque(max_size)
    for command in commands:
        parts = command.split()
        cmd = parts[0]
        if cmd == "push_back":
            deque.push_back(int(parts[1]))
        elif cmd == "push_front":
            deque.push_front(int(parts[1]))
        elif cmd == "pop_front":
            deque.pop_front()
        elif cmd == "pop_back":
            deque.pop_back()

def test_deque():
    print("Test 1: Простые операции")
    commands1 = [
        "push_front 10",
        "push_back 20",
        "pop_front",
        "pop_back",
    ]
    process_commands(commands1, 5)

    print("\nTest 2: Переполнение")
    commands2 = [
        "push_back 1", "push_back 2", "push_back 3", "push_back 4",
        "push_back 5",
    ]
    process_commands(commands2, 4)

    print("\nTest 3: Попытка извлечь из пустого deque")
    commands3 = [
        "pop_back",
        "pop_front",
    ]
    process_commands(commands3, 3)

    print("\nTest 4: Операции на грани максимума")
    commands4 = [
        "push_front 1000000",
        "push_back -1000000",
        "pop_front",
        "pop_back",
    ]
    process_commands(commands4, 2)

    print("\nTest 5: Большое количество операций")
    commands5 = [
        "push_back 1", "push_back 2", "push_back 3", "push_back 4",
        "pop_front", "pop_back",
        "push_front 5", "push_back 6",
        "pop_front", "pop_front",
    ]
    process_commands(commands5, 5)

    print("\nTest 6: Перемешанные push и pop с переполнением и ошибками")
    commands6 = [
        "push_back 100", "push_front 200", "push_back 300", "push_front 400",
        "pop_back",
        "pop_back",
        "pop_back",
        "pop_back",
        "pop_back",
    ]
    process_commands(commands6, 4)

# test_deque()
