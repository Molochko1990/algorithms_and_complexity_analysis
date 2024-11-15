class HashTable:
    def __init__(self, size=100003):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    # при добавлении элемента хэшируем ключ и смотрим есть ли он в таблице
    def put(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return "None"

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return v
        return "None"


def test_hash_table():
    hash_table = HashTable()

    hash_table.put(1, 100)
    assert hash_table.get(1) == 100, "Ошибка: значение для ключа 1 должно быть 100"

    hash_table.put(2, 200)
    assert hash_table.get(2) == 200, "Ошибка: значение для ключа 2 должно быть 200"

    hash_table.put(1, 300)
    assert hash_table.get(1) == 300, "Ошибка: значение для ключа 1 должно быть обновлено до 300"

    assert hash_table.get(3) == "None", "Ошибка: значение для ключа 3 должно быть None"

    assert hash_table.delete(1) == 300, "Ошибка: удаленное значение для ключа 1 должно быть 300"
    assert hash_table.get(1) == "None", "Ошибка: значение для удаленного ключа 1 должно быть None"

    assert hash_table.delete(3) == "None", "Ошибка: удаление несуществующего ключа 3 должно вернуть None"

    for i in range(100):
        hash_table.put(i, i * 10)
    for i in range(100):
        assert hash_table.get(i) == i * 10, f"Ошибка: значение для ключа {i} должно быть {i * 10}"

    print("Все тесты пройдены успешно!")

test_hash_table()


# if __name__ == "__main__":
#     n = int(input())
#     hash_table = HashTable()
#
#     for _ in range(n):
#         query = input().split()
#         command = query[0]
#         key = int(query[1])
#
#         if command == "put":
#             value = int(query[2])
#             hash_table.put(key, value)
#         elif command == "get":
#             print(hash_table.get(key))
#         elif command == "delete":
#             print(hash_table.delete(key))
