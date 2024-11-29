def longest_common_substring(str1, str2):
    m, n = len(str1), len(str2)
    # Создаем таблицу для хранения длины наибольшей общей подстроки
    # dp[i][j] будет содержать длину наибольшей подстроки str1[0..i-1] и str2[0..j-1].
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_len = 0
    substrings = set()

    # Заполняем таблицу dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    substrings = {str1[i - max_len:i]}
                elif dp[i][j] == max_len:
                    substrings.add(str1[i - max_len:i])

    # Возвращаем лексикографически минимальную подстроку
    return min(substrings) if substrings else ""


# Пример использования функции
str1 = "ubrashvabracadabra"
str2 = "calamburashabratha"
result = longest_common_substring(str1, str2)
print(result)  # Вывод: abra
