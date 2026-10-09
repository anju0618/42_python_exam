"""py_redundant_link  (問題文: py_redundant_link.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def redundant_link(edges: list[list[int]]) -> list[int]:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', redundant_link([[1, 2], [1, 3], [2, 3]]), [2, 3])
    check('example 2', redundant_link([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]), [1, 4])
    check('duplicate edge', redundant_link([[1, 2], [1, 2]]), [1, 2])
    check('triangle', redundant_link([[1, 2], [2, 3], [3, 1]]), [3, 1])
    check('cycle in the middle', redundant_link([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]), [1, 3])
    check('long', redundant_link([[2, 7], [7, 8], [3, 6], [2, 5], [6, 8], [4, 8], [2, 8], [1, 8], [7, 10], [3, 9]]), [2, 8])
