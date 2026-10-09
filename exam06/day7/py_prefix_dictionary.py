"""py_prefix_dictionary  (問題文: py_prefix_dictionary.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


class PrefixDictionary:
    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def starts_with(self, prefix: str) -> bool:
        pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    d = PrefixDictionary()
    check('empty: search', d.search('a'), False)
    check('empty: starts_with', d.starts_with('a'), False)
    d.insert('apple')
    check('search apple', d.search('apple'), True)
    check('search app (prefix only)', d.search('app'), False)
    check('starts_with app', d.starts_with('app'), True)
    check('starts_with whole word', d.starts_with('apple'), True)
    check('starts_with longer', d.starts_with('apples'), False)
    d.insert('app')
    check('search app after insert', d.search('app'), True)
    check('search apple still', d.search('apple'), True)
    check('starts_with b', d.starts_with('b'), False)
    d.insert('apple')
    check('duplicate insert is fine', d.search('apple'), True)
    d.insert('b')
    check('single letter', d.search('b'), True)
    check('a is only a prefix', d.search('a'), False)
