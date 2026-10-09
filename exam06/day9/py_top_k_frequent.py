"""py_top_k_frequent  (問題文: py_top_k_frequent.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
    check('example 2', top_k_frequent([1], 1), [1])
    check('tie -> smaller first', top_k_frequent([3, 3, 1, 1, 2], 2), [1, 3])
    check('all distinct', top_k_frequent([5, 4, 3], 3), [3, 4, 5])
    check('negative', top_k_frequent([-1, -1, 2, 2, 2], 1), [2])
    check('k = distinct', top_k_frequent([4, 4, 5, 5, 6], 3), [4, 5, 6])
