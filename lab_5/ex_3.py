def is_match(filename, pattern):
    len_filename = len(filename)
    len_pattern = len(pattern)

    dp = [[False] * (len_pattern + 1) for _ in range(len_filename + 1)] # строим матрицу dp, где dp[i][j] будет True, если подстрока filename[0:i] соответствует подшаблону pattern[0:j].

    dp[0][0] = True # пустая строка соответствует пустому шаблону.

    for j in range(1, len_pattern + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, len_filename + 1):
        for j in range(1, len_pattern + 1):
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                print(dp[i][j])
            elif pattern[j - 1] == '?' or pattern[j - 1] == filename[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[len_filename][len_pattern]

filename = 'ABRACADABRA'
pattern = 'ABRA*ABRA'

if is_match(filename, pattern):
    print("YES")
else:
    print("NO")
