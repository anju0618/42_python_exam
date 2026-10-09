"""py_k_closest  (問題文: py_k_closest.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', k_closest([[1, 3], [-2, 2]], 1), [[-2, 2]])
    check('example 2', k_closest([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]])
    check('tie keeps input order', k_closest([[1, 0], [0, 1], [-1, 0]], 2), [[1, 0], [0, 1]])
    check('k = all', k_closest([[2, 2], [1, 1]], 2), [[1, 1], [2, 2]])
    check('origin', k_closest([[0, 0], [1, 1]], 1), [[0, 0]])
