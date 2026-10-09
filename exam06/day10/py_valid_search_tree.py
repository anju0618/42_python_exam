"""py_valid_search_tree  (問題文: py_valid_search_tree.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def valid_search_tree(root) -> bool:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', valid_search_tree((2, (1, None, None), (3, None, None))), True)
    check('example 2', valid_search_tree((5, (1, None, None), (4, (3, None, None), (6, None, None)))), False)
    check('empty', valid_search_tree(None), True)
    check('deep violation', valid_search_tree((5, (4, None, None), (6, (3, None, None), (7, None, None)))), False)
    check('equal children', valid_search_tree((2, (2, None, None), (2, None, None))), False)
    check('equal left', valid_search_tree((1, (1, None, None), None)), False)
    check('single', valid_search_tree((2147483647, None, None)), True)
    check('valid with inner right', valid_search_tree((3, (1, None, (2, None, None)), (5, None, None))), True)
