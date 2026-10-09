"""py_shortest_cover  (問題文: py_shortest_cover.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def shortest_cover(s: str, t: str) -> str:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', shortest_cover('ADOBECODEBANC', 'ABC'), 'BANC')
    check('example 2', shortest_cover('a', 'a'), 'a')
    check('example 3', shortest_cover('a', 'aa'), '')
    check('duplicates', shortest_cover('aa', 'aa'), 'aa')
    check('single', shortest_cover('ab', 'b'), 'b')
    check('empty t', shortest_cover('abc', ''), '')
    check('order irrelevant', shortest_cover('bba', 'ab'), 'ba')
    check('tie -> leftmost', shortest_cover('abcabc', 'ab'), 'ab')
    check('long', shortest_cover('cabwefgewcwaefgcf', 'cae'), 'cwae')
    check('t longer than s', shortest_cover('ab', 'abc'), '')
