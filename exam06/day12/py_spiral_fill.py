"""py_spiral_fill  (問題文: py_spiral_fill.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def spiral_fill(n: int) -> list[list[int]]:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('n=1', spiral_fill(1), [[1]])
    check('n=2', spiral_fill(2), [[1, 2], [4, 3]])
    check('n=3', spiral_fill(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
    check('n=4', spiral_fill(4), [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
