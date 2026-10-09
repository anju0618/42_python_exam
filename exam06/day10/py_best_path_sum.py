"""py_best_path_sum  (問題文: py_best_path_sum.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def best_path_sum(root) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', best_path_sum((1, (2, None, None), (3, None, None))), 6)
    check('example 2', best_path_sum((-10, (9, None, None), (20, (15, None, None), (7, None, None)))), 42)
    check('single negative', best_path_sum((-3, None, None)), -3)
    check('skip negative child', best_path_sum((2, (-1, None, None), None)), 2)
    check('all negative', best_path_sum((-2, (-1, None, None), None)), -1)
    check('path not through root', best_path_sum((1, (-5, (10, None, None), (10, None, None)), None)), 15)
