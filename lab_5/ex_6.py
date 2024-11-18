from collections import defaultdict

def build_index(documents):
    index = defaultdict(lambda: defaultdict(int))
    for doc_id, document in enumerate(documents):
        for word in document.split():
            index[word][doc_id] += 1
    return index

def search(query, index, num_docs=5):
    relevances = defaultdict(int)
    for word in query.split():
        if word in index:
            for doc_id, count in index[word].items():
                relevances[doc_id] += count

    sorted_docs = sorted(relevances.items(), key=lambda x: (-x[1], x[0]))
    return [doc_id + 1 for doc_id, relevance in sorted_docs[:num_docs]]

def main():
    n = int(input().strip())
    documents = [input().strip() for _ in range(n)]
    m = int(input().strip())
    queries = [input().strip() for _ in range(m)]

    index = build_index(documents)

    results = []
    for query in queries:
        result = search(query, index)
        results.append(" ".join(map(str, result)))

    print("\n".join(results))


def test():
    import sys
    from io import StringIO

    input_data = """3
a b c d e f
a b c d e
a b c
2
a b
f e
"""
    expected_output = """1 2 3
1 2
"""
    sys.stdin = StringIO(input_data)
    sys.stdout = output = StringIO()
    main()
    sys.stdout = sys.__stdout__

    assert output.getvalue() == expected_output, f"Expected:\n{expected_output}\nBut got:\n{output.getvalue()}"
    print("All tests passed!")

test()


'''
Общая суть:
функция билд индекс создает обратный индекс. эта структура данных , которая сопостовляет слова с документами в которых слово встречается. это позволяет быстро выполнять полнотекстовый поиск


'''