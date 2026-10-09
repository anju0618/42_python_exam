"""py_text_distance  (問題文: py_text_distance.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def text_distance(a: str, b: str) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', text_distance('horse', 'ros'), 3)
    check('example 2', text_distance('intention', 'execution'), 5)
    check('both empty', text_distance('', ''), 0)
    check('delete all', text_distance('abc', ''), 3)
    check('insert all', text_distance('', 'abc'), 3)
    check('same', text_distance('same', 'same'), 0)
    check('kitten', text_distance('kitten', 'sitting'), 3)
    check('one replace', text_distance('a', 'b'), 1)
    check('reverse', text_distance('abc', 'cba'), 2)
