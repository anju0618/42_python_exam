def generate_spiral(n: int) -> list[list[int]]:


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('3x3 spiral', generate_spiral(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
    check('1x1 spiral', generate_spiral(1), [[1]])
    check('2x2 spiral', generate_spiral(2), [[1, 2], [4, 3]])
    check('4x4 spiral', generate_spiral(4), [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
    check('5x5 spiral', generate_spiral(5), [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]])
    check('6x6 spiral', generate_spiral(6), [[1, 2, 3, 4, 5, 6], [20, 21, 22, 23, 24, 7], [19, 32, 33, 34, 25, 8], [18, 31, 36, 35, 26, 9], [17, 30, 29, 28, 27, 10], [16, 15, 14, 13, 12, 11]])
