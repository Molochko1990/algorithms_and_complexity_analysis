def is_non_decreasing_heap(arr):
    n = len(arr)
    for i in range(n):
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        if left_child_index < n and arr[i] > arr[left_child_index]:
            return "NO"

        if right_child_index < n and arr[i] > arr[right_child_index]:
            return "NO"

    return "YES"


def run_tests():
    arr1 = [1, 2, 3, 4, 5, 6]
    assert is_non_decreasing_heap(arr1) == "YES", f"Test 1 Failed: {arr1}"

    arr2 = [10, 9, 8, 7, 6, 5]
    assert is_non_decreasing_heap(arr2) == "NO", f"Test 2 Failed: {arr2}"

    arr3 = [5, 5, 5, 5, 5, 5]
    assert is_non_decreasing_heap(arr3) == "YES", f"Test 3 Failed: {arr3}"

    arr4 = [42]
    assert is_non_decreasing_heap(arr4) == "YES", f"Test 4 Failed: {arr4}"

    arr5 = [10**9, 10**9, 10**9, 10**9, 10**9, 10**9]
    assert is_non_decreasing_heap(arr5) == "YES", f"Test 5 Failed: {arr5}"

    arr6 = [-10**9, -10**9, -10**9, -10**9, -10**9, -10**9]
    assert is_non_decreasing_heap(arr6) == "YES", f"Test 6 Failed: {arr6}"

    print("All tests passed!")

run_tests()