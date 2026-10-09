"""py_room_planner  (問題文: py_room_planner.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def room_planner(meetings: list[list[int]]) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', room_planner([[0, 30], [5, 10], [15, 20]]), 2)
    check('example 2', room_planner([[7, 10], [2, 4]]), 1)
    check('empty', room_planner([]), 0)
    check('touching', room_planner([[1, 5], [5, 10]]), 1)
    check('all overlap', room_planner([[1, 5], [2, 6], [3, 7]]), 3)
    check('one big + small chain', room_planner([[1, 10], [2, 3], [3, 4], [4, 5]]), 2)
    check('unsorted input', room_planner([[15, 20], [0, 30], [5, 10]]), 2)
    check('same time', room_planner([[1, 2], [1, 2], [1, 2]]), 3)
