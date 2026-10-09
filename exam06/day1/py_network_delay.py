"""py_network_delay  (問題文: py_network_delay.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def network_delay(times: list[list[int]], n: int, k: int) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', network_delay([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2)
    check('example 2', network_delay([[1, 2, 1]], 2, 1), 1)
    check('unreachable', network_delay([[1, 2, 1]], 2, 2), -1)
    check('single node', network_delay([], 1, 1), 0)
    check('shortcut vs direct', network_delay([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1), 3)
    check('detour is shorter', network_delay([[1, 2, 5], [1, 3, 1], [3, 2, 1]], 3, 1), 2)
    check('one-way only', network_delay([[1, 2, 1], [3, 2, 1]], 3, 1), -1)
    check('chain', network_delay([[1, 2, 3], [2, 3, 3], [3, 4, 3]], 4, 1), 9)
