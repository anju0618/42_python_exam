"""py_gas_loop  (問題文: py_gas_loop.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def gas_loop(gas: list[int], cost: list[int]) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', gas_loop([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
    check('example 2', gas_loop([2, 3, 4], [3, 4, 3]), -1)
    check('single ok', gas_loop([5], [4]), 0)
    check('single no', gas_loop([4], [5]), -1)
    check('start 0', gas_loop([3, 1, 1], [1, 2, 2]), 0)
    check('end of list', gas_loop([1, 1, 5], [2, 2, 1]), 2)
