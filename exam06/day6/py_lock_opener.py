"""py_lock_opener  (問題文: py_lock_opener.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def lock_opener(deadends: list[str], target: str) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', lock_opener(['0201', '0101', '0102', '1212', '2002'], '0202'), 6)
    check('example 2 (wrap)', lock_opener(['8888'], '0009'), 1)
    check('example 3 (surrounded)', lock_opener(['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'], '8888'), -1)
    check('already there', lock_opener([], '0000'), 0)
    check('start is deadend', lock_opener(['0000'], '8888'), -1)
    check('one step up', lock_opener([], '1000'), 1)
    check('one step down (wrap)', lock_opener([], '9000'), 1)
    check('all neighbours dead', lock_opener(['0001', '0009', '0010', '0090', '0100', '0900', '1000', '9000'], '0002'), -1)
    check('far', lock_opener([], '5555'), 20)
    check('target is deadend', lock_opener(['0202'], '0202'), -1)
