"""py_alien_order  (問題文: py_alien_order.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def alien_order(words: list[str]) -> str:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', alien_order(['wrt', 'wrf', 'er', 'ett', 'rftt']), 'wertf')
    check('example 2', alien_order(['z', 'x']), 'zx')
    check('cycle', alien_order(['z', 'x', 'z']), '')
    check('prefix after longer', alien_order(['abc', 'ab']), '')
    check('single word', alien_order(['a']), 'a')
    check('free letters, smallest first', alien_order(['ab', 'adc']), 'abcd')
    check('same words', alien_order(['a', 'a']), 'a')
    check('empty list', alien_order([]), '')
