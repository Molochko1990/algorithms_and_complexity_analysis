import time
from memory_profiler import profile


@profile
def search_in_rotated_array(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

def run_tests():
    start_time = time.time()
    index = search_in_rotated_array([10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8)
    end_time = time.time()

    print(f"Input Array: {[10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9]}")
    print(f"Target: 8")
    print(f"Index: {index}")
    print(f"Time taken: {end_time - start_time} seconds")
    print("")

run_tests()