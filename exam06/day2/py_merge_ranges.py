"""py_merge_ranges  (問題文: py_merge_ranges.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def merge_ranges(ranges: list[list[int]]) -> list[list[int]]:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', merge_ranges([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
    check('example 2', merge_ranges([[1, 4], [4, 5]]), [[1, 5]])
    check('empty', merge_ranges([]), [])
    check('unsorted', merge_ranges([[5, 6], [1, 2]]), [[1, 2], [5, 6]])
    check('contained', merge_ranges([[1, 10], [2, 3]]), [[1, 10]])
    check('zero range', merge_ranges([[1, 4], [0, 0]]), [[0, 0], [1, 4]])
    check('one swallows all', merge_ranges([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]), [[1, 10]])
    check('single', merge_ranges([[3, 3]]), [[3, 3]])
