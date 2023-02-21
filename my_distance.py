import typing
import sys


def ineffective_minimal_distance(word1: str, word2: str) -> int:
    """
    recursive solution without memoization will make your laptop cozy and warm
    time complexity: O(3^m)
    space complexity: O(m)
    """
    m, n = len(word1), len(word2)

    def md_recursive(
        word1: str, word2: str, word1_length: int, word2_length: int
    ) -> int:
        if word1_length == 0:
            return word2_length
        if word2_length == 0:
            return word1_length
        if word1[word1_length - 1] == word2[word2_length - 1]:
            return md_recursive(word1, word2, word1_length - 1, word2_length - 1)
        else:
            return (
                min(
                    md_recursive(word1, word2, word1_length, word2_length - 1),
                    md_recursive(word1, word2, word1_length - 1, word2_length),
                    md_recursive(word1, word2, word1_length - 1, word2_length - 1),
                )
                + 1
            )

    return md_recursive(word1, word2, m, n)


def recursive_minimal_distance(word1: str, word2: str) -> int:
    """
    recursive solution with memoization
    time complexity: O(mn)
    space complexity: O(mn)
    """
    m, n = len(word1), len(word2)
    memo = [[-1] * (n + 1) for _ in range(m + 1)]

    def md_recursive(
        word1: str, word2: str, word1_length: int, word2_length: int
    ) -> int:
        if word1_length == 0:
            return word2_length
        if word2_length == 0:
            return word1_length
        if memo[word1_length][word2_length] != -1:
            return memo[word1_length][word2_length]
        if word1[word1_length - 1] == word2[word2_length - 1]:
            memo[word1_length][word2_length] = md_recursive(
                word1, word2, word1_length - 1, word2_length - 1
            )
        else:
            memo[word1_length][word2_length] = (
                min(
                    md_recursive(word1, word2, word1_length, word2_length - 1),
                    md_recursive(word1, word2, word1_length - 1, word2_length),
                    md_recursive(word1, word2, word1_length - 1, word2_length - 1),
                )
                + 1
            )
        return memo[word1_length][word2_length]

    return md_recursive(word1, word2, m, n)


def minimal_distance(word1: str, word2: str) -> int:
    """
    iterative solution with memoization, we aware of recursion limit
    where memo[i][j] = minimal distance between word1[:i] and word2[:j]
    time complexity: O(mn)
    space complexity: O(mn)
    """
    m, n = len(word1), len(word2)
    memo = [[-1] * (n + 1) for _ in range(m + 1)]  # +1 for empty string

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:  # word1 is empty
                memo[i][j] = j
            elif j == 0:  # word2 is empty
                memo[i][j] = i
            elif word1[i - 1] == word2[j - 1]:  # last characters are the same
                memo[i][j] = memo[i - 1][j - 1]
            else:  # last characters are different
                memo[i][j] = (
                    min(
                        memo[i][j - 1],  # deletion
                        memo[i - 1][j],  # insertion
                        memo[i - 1][j - 1],  # substitution
                    )
                    + 1
                )  # +1 for the operation

    result = memo[m][n]

    def backtrace(w1, w2) -> typing.List[str]:
        """
        backtrace the path from w2 to w1 using memo
        make changes in temp string:
            add "_" for deletion and capitalize for insertion/substitution
        time complexity: O(m + n)
        spce complexity: O(m + n)
        """
        i, j = m, n
        mutation_temp = w1
        changes = [mutation_temp]
        while i > 0 or j > 0:
            if i > 0 and j > 0 and w1[i - 1] == w2[j - 1]:  # no change
                i, j = i - 1, j - 1
                continue
            elif j > 0 and memo[i][j] == memo[i][j - 1] + 1:  # deletion
                mutation_temp = (
                    mutation_temp[:i] + w2[j - 1].capitalize() + mutation_temp[i:]
                )
                j -= 1
            elif i > 0 and memo[i][j] == memo[i - 1][j] + 1:  # insertion
                mutation_temp = mutation_temp[: i - 1] + "_" + mutation_temp[i:]
                i -= 1
            elif i > 0 and j > 0 and memo[i][j] == memo[i - 1][j - 1] + 1:  # substitution
                mutation_temp = (
                    mutation_temp[: i - 1] + w2[j - 1].capitalize() + mutation_temp[i:]
                )
                i, j = i - 1, j - 1
            changes.append(mutation_temp)
        return changes[::-1]

    print("\n".join(backtrace(word1, word2)), f"\n{result=}")
    return result


if __name__ == "__main__":
    word1, word2 = sys.argv[1:3]
    distance = minimal_distance(word1, word2)
    print(distance)
