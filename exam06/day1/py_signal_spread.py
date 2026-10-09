"""py_signal_spread  (問題文: py_signal_spread.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def signal_spread(grid: list[list[int]]) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', signal_spread([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4)
    check('example 2 (isolated receiver)', signal_spread([[2, 1, 1], [0, 1, 1], [1, 0, 1]]), -1)
    check('no receiver', signal_spread([[0, 2]]), 0)
    check('only empty', signal_spread([[0]]), 0)
    check('lone receiver', signal_spread([[1]]), -1)
    check('two sources', signal_spread([[2, 2], [1, 1]]), 1)
    check('row, two sources', signal_spread([[1, 2, 1, 1, 2, 1, 1]]), 2)
    check('wall blocks', signal_spread([[2, 0, 1]]), -1)
