"""py_queens_count  (問題文: py_queens_count.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def queens_count(n: int) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('n=1', queens_count(1), 1)
    check('n=2', queens_count(2), 0)
    check('n=3', queens_count(3), 0)
    check('n=4', queens_count(4), 2)
    check('n=5', queens_count(5), 10)
    check('n=6', queens_count(6), 4)
    check('n=7', queens_count(7), 40)
    check('n=8', queens_count(8), 92)
