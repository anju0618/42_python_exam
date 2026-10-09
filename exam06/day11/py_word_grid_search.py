"""py_word_grid_search  (問題文: py_word_grid_search.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def word_grid_search(board: list[list[str]], words: list[str]) -> list[str]:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', word_grid_search([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']], ['oath', 'pea', 'eat', 'rain']), ['oath', 'eat'])
    check('example 2 (reuse)', word_grid_search([['a', 'b'], ['c', 'd']], ['abcb']), [])
    check('1x1', word_grid_search([['a']], ['a', 'b']), ['a'])
    check('keeps words order', word_grid_search([['a', 'b']], ['ba', 'ab', 'b']), ['ba', 'ab', 'b'])
    check('no words', word_grid_search([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']], []), [])
    check('snake', word_grid_search([['a', 'b'], ['d', 'c']], ['abcd', 'adcb', 'ac']), ['abcd', 'adcb'])
