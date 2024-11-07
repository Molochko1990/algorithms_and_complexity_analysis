def can_divide_chapters(chapters, max_pages, k):
    current_sum = 0
    required_volumes = 1

    for pages in chapters:
        if current_sum + pages > max_pages:
            required_volumes += 1
            current_sum = pages
            if required_volumes > k:
                return False
        else:
            current_sum += pages

    return True


def find_min_max_volume(chapters, k):
    left = max(chapters) # глава с максимальным кол-вом страниц
    right = sum(chapters) # общая сумма страниц всех глав

    while left < right:
        mid = (left + right) // 2

        if can_divide_chapters(chapters, mid, k):
            right = mid
        else:
            left = mid + 1

    return left


def main():
    with open('INPUT.txt', 'r') as file:
        n = int(file.readline().strip())
        chapters = list(map(int, file.readline().strip().split()))
        k = int(file.readline().strip())

    result = find_min_max_volume(chapters, k)

    with open('OUTPUT.txt', 'w') as file:
        file.write(str(result) + '\n')


if __name__ == "__main__":
    main()
