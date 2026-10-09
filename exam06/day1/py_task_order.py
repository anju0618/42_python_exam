"""py_task_order  (問題文: py_task_order.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def task_order(n: int, prereqs: list[list[int]]) -> list[int]:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', task_order(2, [[1, 0]]), [0, 1])
    check('example 2', task_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]), [0, 1, 2, 3])
    check('cycle', task_order(2, [[0, 1], [1, 0]]), [])
    check('no prereqs', task_order(3, []), [0, 1, 2])
    check('n = 0', task_order(0, []), [])
    check('smallest first', task_order(3, [[0, 2]]), [1, 2, 0])
    check('two roots', task_order(4, [[0, 3], [1, 3]]), [2, 3, 0, 1])
    check('self loop', task_order(1, [[0, 0]]), [])
    check('cycle after a valid part', task_order(4, [[1, 0], [2, 3], [3, 2]]), [])
