"""py_word_hunt  (問題文: py_word_hunt.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""

BOARD = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]



def word_hunt(board: list[list[str]], word: str) -> bool:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', word_hunt(BOARD, 'ABCCED'), True)
    check('example 2', word_hunt(BOARD, 'SEE'), True)
    check('example 3 (reuse)', word_hunt(BOARD, 'ABCB'), False)
    check('1x1 match', word_hunt([['a']], 'a'), True)
    check('1x1 no match', word_hunt([['a']], 'b'), False)
    check('reuse not allowed', word_hunt([['a', 'a']], 'aaa'), False)
    check('backwards', word_hunt([['a', 'b']], 'ba'), True)
    check('word longer than board', word_hunt([['a', 'b']], 'abab'), False)
    check('diagonal is not adjacent', word_hunt([['a', 'b'], ['c', 'd']], 'ad'), False)
    check('snake', word_hunt([['a', 'b'], ['d', 'c']], 'abcd'), True)
