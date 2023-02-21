def minimal_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0 for _ in range(n)] for _ in range(m)]

    def get_dp(i: int, j: int) -> int:
        """
        Returns the value of dp[i][j] if it exists
        """
        if i < 0 and j < 0:
            return 0
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        return dp[i][j]

    for i in range(m):
        for j in range(n):
            deletion = get_dp(i, j - 1) + 1
            insertion = get_dp(i - 1, j) + 1
            substitution = get_dp(i - 1, j - 1) + (0 if word1[i] == word2[j] else 1)
            dp[i][j] = min(deletion, insertion, substitution)

    distance = answer = get_dp(m - 1, n - 1)
    print(distance)
    cur_i = m - 1
    cur_j = n - 1
    cur_word = list(word2)

    print("".join(cur_word))
    while distance > 0:
        deletion = get_dp(cur_i, cur_j - 1)
        insertion = get_dp(cur_i - 1, cur_j)
        substitution = get_dp(cur_i - 1, cur_j - 1)
        if substitution < distance:
            cur_word[cur_j] = word1[cur_i] if word1 else ""
            cur_i -= 1
            cur_j -= 1
            distance = substitution
            print("".join(cur_word))
        elif deletion < distance:
            cur_word.pop(cur_j)
            cur_j -= 1
            distance = deletion
            print("".join(cur_word))
        elif insertion < distance:
            cur_word.insert(cur_j + 1, word1[cur_i])
            cur_i -= 1
            distance = insertion
            print("".join(cur_word))
        else:
            cur_i -= 1
            cur_j -= 1
    return answer


if __name__ == "__main__":
    import sys

    minimal_distance(sys.argv[1], sys.argv[2])
