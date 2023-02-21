def insert_into_array(arr, index, new_item):  # wrong name, should be insert_into_array
    return arr[:index] + [new_item] + arr[index:1]  # can be replaced with arr.insert(index, new_item)


def minimal_distance(word1, word2):
    """
    time complexity: O(mn)
    space complexity: O(mn)
    """
    n = len(word1)  # confusing order of variables not alphabetically (n, m) -> (m, n).
    m = len(word2)
    dp = [[0 for _ in range(n)] for _ in range(m)]  # should be another order?

    def get_dp(i, j):
        # this function is not needed, we can just use dp[i][j] instead
        # it breaks readability
        if i < 0 or j < 0:
            return 0
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        return dp[i][j]

    for i in range(n):
        for j in range(m):
            dp[i][j] = min(
                get_dp(i - 1, j) + 1,
                get_dp(i, j - 1) + 1,
                get_dp(i - 1, j - 1) + (0 if word1[i] == word2[j] else 1),
            )  # if exception will be raised, it will be hard to find the reason

    distance = get_dp(n - 1, m - 1)
    print(distance)  # avoid print statements, use logging or return value
    # ^ this value will be reused in the next loop, so it should be stored in a variable
    cur_i = n - 1
    cur_j = m - 1
    cur_word = list(word2)

    print("".join(cur_word))
    while distance > 0:  # imho this code hard to understand
        deletion = get_dp(cur_i, cur_j - 1)
        insertion = get_dp(cur_i - 1, cur_j)
        substitution = get_dp(cur_i - 1, cur_j - 1)
        if substitution < distance:
            cur_word[cur_j] = word1[cur_i]  # if word1 is empty, it will raise an exception
            cur_i -= 1
            cur_j -= 1
            distance = substitution
            print("".join(cur_word))
        elif deletion < distance:
            cur_word[cur_j] = ""  # can be replaced with cur_word.pop(cur_j)
            cur_j -= 1
            distance = deletion
            print("".join(cur_word))
        elif insertion < distance:
            cur_word = insert_into_array(cur_word, cur_j + 1, word1[cur_i])  # bad code style
            cur_i -= 1
            distance = insertion
            print("".join(cur_word))
        else:
            cur_i -= 1
            cur_j -= 1
    # code dont return anything, hard to test


if __name__ == "__main__":
    import sys  # bad code style, should be at the top of the file

    minimal_distance(sys.argv[1], sys.argv[2])
