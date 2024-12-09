class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False


def maximum_spanning_tree(n, edges): # эта функция отвечает за нахождение минимального остовного дерева
    edges.sort(key=lambda x: -x[2])

    dsu = DisjointSetUnion(n) # тут сортируем ребра в порядке убывания весов, чтобы смотреть на те которые больше весят
    max_tree_weight = 0
    edges_used = 0

    for u, v, w in edges:
        if dsu.union(u - 1, v - 1):
            max_tree_weight += w
            edges_used += 1
            if edges_used == n - 1:
                break

    if edges_used == n - 1: # если добавлен н-1 ребер, то успешно завершено, иначе граф несвязный.
        return max_tree_weight
    else:
        return "Oops! I did it again"


n = 4
edges = [
    (1, 2, 5),
    (1, 3, 6),
    (2, 4, 8),
    (3, 4, 3)
]

result = maximum_spanning_tree(n, edges)
print(result)

# общая суть задачи соединить все ребра оставив минимальное кол-во ребер. И ребра оставить по возможности те, которые больше всего весят.
