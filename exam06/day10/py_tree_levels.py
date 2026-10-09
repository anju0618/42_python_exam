"""py_tree_levels  (問題文: py_tree_levels.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def tree_levels(root) -> list[list[int]]:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', tree_levels((3, (9, None, None), (20, (15, None, None), (7, None, None)))), [[3], [9, 20], [15, 7]])
    check('empty', tree_levels(None), [])
    check('single', tree_levels((1, None, None)), [[1]])
    check('left chain', tree_levels((1, (2, (3, None, None), None), None)), [[1], [2], [3]])
    check('right only', tree_levels((1, None, (2, None, None))), [[1], [2]])
