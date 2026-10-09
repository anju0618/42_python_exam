"""py_bracket_builder  (問題文: py_bracket_builder.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def bracket_builder(n: int) -> list[str]:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('n=1', bracket_builder(1), ['()'])
    check('n=2', bracket_builder(2), ['(())', '()()'])
    check('n=3', bracket_builder(3), ['((()))', '(()())', '(())()', '()(())', '()()()'])
    check('n=4 count', bracket_builder(4), ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()'])
