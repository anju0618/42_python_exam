"""py_paths_with_walls  (問題文: py_paths_with_walls.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def paths_with_walls(grid: list[list[int]]) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', paths_with_walls([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)
    check('example 2', paths_with_walls([[0, 1], [0, 0]]), 1)
    check('start is wall', paths_with_walls([[1, 0]]), 0)
    check('1x1', paths_with_walls([[0]]), 1)
    check('blocked row', paths_with_walls([[0, 0], [1, 1]]), 0)
    check('open 2x3', paths_with_walls([[0, 0, 0], [0, 0, 0]]), 3)
    check('goal is wall', paths_with_walls([[0, 0], [0, 1]]), 0)
    check('open 4x4', paths_with_walls([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]), 20)
