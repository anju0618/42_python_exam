"""py_pack_strings  (問題文: py_pack_strings.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def pack(strs: list[str]) -> str:
    pass


def unpack(s: str) -> list[str]:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    for i, strs in enumerate([[], [''], ['', ''], ['hello', 'world'], ['a#b', '3#abc', '#'], ['\n', ' '],
                              ['ab', '', 'cd'], ['1', '2', '3'], ['::', ';'], ['10#aaaaaaaaaa'], ['0#', '0'],
                              ['x' * 1000, 'y']]):
        check(f'roundtrip {i}: {strs!r:.40}', unpack(pack(strs)), strs)
    check('pack returns str', isinstance(pack(['a']), str), True)
    check('[] and [""] differ', pack([]) != pack(['']), True)
