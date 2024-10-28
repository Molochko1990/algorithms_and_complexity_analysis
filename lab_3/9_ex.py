import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000)


def build_tree(n, edges):
    tree = defaultdict(list)
    for u, v, w in edges:
        tree[u].append((v, w))
        tree[v].append((u, w))
    return tree


def dfs(tree, node, parent, depth, dist, dp):
    dp[node][0] = parent
    for neigh, weight in tree[node]:
        if neigh != parent:
            dist[neigh] = dist[node] + weight
            depth[neigh] = depth[node] + 1
            dfs(tree, neigh, node, depth, dist, dp)


def preprocess_lca(n, dp, depth):
    max_log = len(dp[0])
    for i in range(1, max_log):
        for node in range(n):
            if dp[node][i - 1] != -1:
                dp[node][i] = dp[dp[node][i - 1]][i - 1]


def find_lca(u, v, dp, depth):
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    max_log = len(dp[0])
    for i in range(max_log):
        if (diff >> i) & 1:
            u = dp[u][i]

    if u == v:
        return u

    for i in reversed(range(max_log)):
        if dp[u][i] != dp[v][i]:
            u = dp[u][i]
            v = dp[v][i]

    return dp[u][0]


def query_distances(n, queries, tree):
    depth = [0] * n   # глубина каждой вершины [0, 1, 1, 2, 2, 2]
    dist = [0] * n  # расстояние от корня до каждой вершины [0, 4, 3, 6, 5, 10]
    max_log = 17
    dp = [[-1] * max_log for _ in range(n)]  # таблица предков по двоичной системе для каждой вершины. заполняется в preprocess_lca

    root = 0
    dfs(tree, root, -1, depth, dist, dp)
    preprocess_lca(n, dp, depth)

    results = []
    for u, v in queries:
        lca = find_lca(u, v, dp, depth)
        distance = dist[u] + dist[v] - 2 * dist[lca]
        results.append(distance)

    return results




def test_manual():
    # Пример дерева:
    #     0
    #    / \
    #   1   2
    #  / \   \
    # 3   4   5
    #
    # Ребра: (u, v, w)
    edges = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 3, 2),
        (1, 4, 1),
        (2, 5, 7)
    ]
    n = 6
    queries = [
        (3, 4),
        (3, 5),
        (0, 5),
        (4, 5),
    ]

    tree = build_tree(n, edges)
    results = query_distances(n, queries, tree)

    print("Результаты тестов:")
    for query, result in zip(queries, results):
        print(f"Расстояние между вершинами {query[0]} и {query[1]}: {result}")


test_manual()

# 1) строим дерево
# 2) обход дфс для нахождения глубины для каждой вершины
# 3) препроцесс лса (лоуест комон энсестр) эта функция позволяет логарифмически находит общего предка
# 4) лса. находим общего предка для вершин
# 5) вычисляем расстояние query_distance
#


#  4)смысл поиска общей вершины в том, что мы сначала выравниваем обе вершины на один "горизонтальный" уровень,
#  4)затем если уровни равны то одновременно берем предков для обоих вершин. и ищем общего предка