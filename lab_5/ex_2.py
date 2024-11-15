import os

class Redis:
    def __init__(self, db_filename='database.txt', index_filename='index.txt'):
        self.db_filename = db_filename
        self.index_filename = index_filename
        self.index = {}
        if os.path.exists(self.index_filename): # Если мы ранее использовали нашу бд, то данная функция найдет в ней индекс и запишет в словарь, который исползьуется во время работы кода.
                                                # То есть мы не в оперативке храним а именно на диске
            with open(self.index_filename, 'r') as f:
                for line in f:
                    key, pos = line.strip().split(',')
                    self.index[key] = int(pos)

    def save_index(self):
        with open(self.index_filename, 'w') as f:
            for key, pos in self.index.items():
                f.write(f"{key},{pos}\n")

    def add(self, key, value):
        if key in self.index:
            print("ERROR")
            return
        with open(self.db_filename, 'a') as f:
            pos = f.tell()
            f.write(f"{key}:{value}\n")
            self.index[key] = pos
            print(self.index)
        self.save_index()

    def delete(self, key):
        if key not in self.index:
            print("ERROR")
            return
        del self.index[key]
        self.save_index()

    def update(self, key, value):
        if key not in self.index:
            print("ERROR")
            return
        self.delete(key)
        self.add(key, value)

    def print(self, key):
        if key not in self.index:
            print("ERROR")
            return
        pos = self.index[key]
        with open(self.db_filename, 'r') as f:
            f.seek(pos)
            line = f.readline().strip()
            print(line)

'''
общая суть: у нас есть бд, которая сохраняет данные между запусками программы. 
1) если индекс существует (в файле index), то из него берутся данные, которые содержат ссылку на позицию куда записывать данные в бд
2) при add значения проверяется есть ли значение в индексе (который словарь (в оперативке)). если есть - еррор, иначе добавляется.
3)delete update  в целом аналогично
'''


def test_database_operations():
    db = Redis()

    db.add("key1", "value1")
    db.add("key2", "value2")

    db.print("key1")

    db.update("key1", "new_value1")
    db.print("key1")

    db.delete("key2")
    db.print("key2")

    db.add("key1", "another_value")

    db.delete("key3")

    db.update("key3", "new_value")

    db.print("key1")

test_database_operations()
