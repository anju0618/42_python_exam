"""py_multiply_strings  (問題文: py_multiply_strings.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def multiply_strings(a: str, b: str) -> str:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', multiply_strings('2', '3'), '6')
    check('example 2', multiply_strings('123', '456'), '56088')
    check('zero', multiply_strings('0', '9999'), '0')
    check('nines', multiply_strings('999', '999'), '998001')
    check('one', multiply_strings('1', '12345'), '12345')
    check('big', multiply_strings('123456789123456789', '987654321987654321'), '121932631356500531347203169112635269')
    check('zero both', multiply_strings('0', '0'), '0')
