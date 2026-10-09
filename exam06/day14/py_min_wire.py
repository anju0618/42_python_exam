"""py_min_wire  (問題文: py_min_wire.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def min_wire(points: list[list[int]]) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', min_wire([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20)
    check('example 2', min_wire([[3, 12], [-2, 5], [-4, 1]]), 18)
    check('single', min_wire([[0, 0]]), 0)
    check('two', min_wire([[0, 0], [1, 1]]), 2)
    check('same point', min_wire([[1, 1], [1, 1]]), 0)
    check('line', min_wire([[0, 0], [0, 1], [0, 2], [0, 3]]), 3)
    check('grid 3x3', min_wire([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]), 8)
