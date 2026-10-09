"""py_decode_ways  (問題文: py_decode_ways.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def decode_ways(s: str) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', decode_ways('12'), 2)
    check('example 2', decode_ways('226'), 3)
    check('example 3', decode_ways('06'), 0)
    check('zero', decode_ways('0'), 0)
    check('ten', decode_ways('10'), 1)
    check('27', decode_ways('27'), 1)
    check('one digit', decode_ways('1'), 1)
    check('11106', decode_ways('11106'), 2)
    check('100', decode_ways('100'), 0)
    check('empty', decode_ways(''), 0)
    check('long (needs DP)', decode_ways('1111111111111111111111111111111111111111'), 165580141)
