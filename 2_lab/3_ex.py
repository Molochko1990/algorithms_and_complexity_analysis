from memory_profiler import profile


@profile()
def max_possible_product(arr):
    arr.sort()
    n = len(arr)

    max_product = max(arr[n - 1] * arr[n - 2] * arr[n - 3], arr[0] * arr[1] * arr[n - 1])

    return max_product


array = [-7, -2, 1, 2, 3, 4, 5, 6]
result = max_possible_product(array)
print(result)
