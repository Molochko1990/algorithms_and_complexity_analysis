def read_sets(file_path):
    with open(file_path, 'r') as file:

        first_line = file.readline().strip()
        N, M, K = map(int, first_line.split()) # N-множества для проверки M-колво элементов в множествх K-эталонные элементы

        reference_sets = set() # тут храним эталонные множества
        for _ in range(N):
            elements = map(int, file.readline().strip().split())
            reference_sets.add(frozenset(elements))

        results = [] # тут хранится результат для каждого из эталонных множеств
        for _ in range(K): # проходится по каждому из оставшивхся множеств и сравнивает с эталонными
            elements = map(int, file.readline().strip().split())
            trial_set = frozenset(elements)
            if trial_set in reference_sets:
                results.append('1')
            else:
                results.append('0')

    return results

def main():
    file_path = 'input_ex8.txt'
    results = read_sets(file_path)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
