#!/user/bin/env python3
"""
bleh
"""

nums = [1, 2, 2, 3]


def get_subset(n : list[int] ):
    """
    bleh
    """

    result: list[int] = []
    n.sort()

    def backtrack(i, subset):

        if i == len(n):
            result.append(subset[::])
            return

        # all that include i
        subset.append(n[i])
        backtrack(i+1, subset)
        subset.pop()
        # all that don't include
        # skipping over dups
        while i + 1 < len(n) and n[i] == n[i+1]:
            i += 1
        backtrack(i+1, subset)

    backtrack(0, [])
    return result


print(get_subset(nums))
