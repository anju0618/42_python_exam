"""py_word_split  (問題文: py_word_split.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def word_split(s: str, words: list[str]) -> bool:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', word_split('leetcode', ['leet', 'code']), True)
    check('example 2', word_split('applepenapple', ['apple', 'pen']), True)
    check('example 3', word_split('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']), False)
    check('empty s', word_split('', ['a']), True)
    check('no words', word_split('a', []), False)
    check('7 = 4 + 3', word_split('aaaaaaa', ['aaaa', 'aaa']), True)
    check('7 is odd', word_split('aaaaaaa', ['aaaa', 'aa']), False)
    check('prefix trap', word_split('abcd', ['a', 'abc', 'b', 'cd']), True)
    check('slow if naive', word_split('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', ['a', 'aa', 'aaa', 'aaaa']), False)
