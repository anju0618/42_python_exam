"""py_equal_split  (問題文: py_equal_split.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def equal_split(nums: list[int]) -> bool:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', equal_split([1, 5, 11, 5]), True)
    check('example 2', equal_split([1, 2, 3, 5]), False)
    check('single', equal_split([1]), False)
    check('pair', equal_split([2, 2]), True)
    check('1 1', equal_split([1, 1]), True)
    check('odd total', equal_split([1, 2, 5]), False)
    check('four threes', equal_split([3, 3, 3, 3]), True)
    check('big', equal_split([100, 100, 100, 100, 100, 99, 1]), True)
