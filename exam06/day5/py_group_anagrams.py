"""py_group_anagrams  (問題文: py_group_anagrams.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def group_anagrams(words: list[str]) -> list[list[str]]:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
    check('example 2', group_anagrams(['']), [['']])
    check('single', group_anagrams(['a']), [['a']])
    check('empty list', group_anagrams([]), [])
    check('no anagrams', group_anagrams(['ab', 'cd']), [['ab'], ['cd']])
    check('duplicates', group_anagrams(['a', 'a']), [['a', 'a']])
    check('order of first appearance', group_anagrams(['b', 'a', 'b']), [['b', 'b'], ['a']])
