"""py_min_jumps  (問題文: py_min_jumps.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def min_jumps(nums: list[int]) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', min_jumps([2, 3, 1, 1, 4]), 2)
    check('example 2', min_jumps([2, 3, 0, 1, 4]), 2)
    check('single', min_jumps([0]), 0)
    check('one jump', min_jumps([1, 2]), 1)
    check('all ones', min_jumps([1, 1, 1, 1]), 3)
    check('big jump', min_jumps([10, 1, 1, 1]), 1)
