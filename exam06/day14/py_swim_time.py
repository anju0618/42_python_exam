"""py_swim_time  (問題文: py_swim_time.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def swim_time(grid: list[list[int]]) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', swim_time([[0, 2], [1, 3]]), 3)
    check('example 2', swim_time([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]), 16)
    check('1x1', swim_time([[0]]), 0)
    check('start is high', swim_time([[3, 0], [1, 2]]), 3)
    check('3x3', swim_time([[0, 1, 2], [7, 8, 3], [6, 5, 4]]), 4)
