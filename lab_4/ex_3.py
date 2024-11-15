def max_intersection_size(sets):
    max_size = 0
    n = len(sets) # сколько всего множеств

    # идем по каждому множеству и сравниваем его с каждым множеством.
    for i in range(n):
        for j in range(i + 1, n):
            intersection_size = manual_intersection_size(sets[i], sets[j])
            if intersection_size > max_size:
                max_size = intersection_size

    return max_size

# сравниваем элементы у двух выбранных множеств на предмет пересечения
def manual_intersection_size(set1, set2):
    intersection_count = 0
    for elem in set1:
        if elem in set2:
            intersection_count += 1
    return intersection_count


sets = [
    {1, 2, 3, 4, 5},
    {4, 5, 6, 7, 8},
    {5, 6, 7, 8, 9},
    {1, 5, 9, 10, 11}
]





print("Максимальный размер пересечения:", max_intersection_size(sets))



# смысл задачи найти из представленных множеств новое множество с наибольшим кол-вом пересекающихся элементов
