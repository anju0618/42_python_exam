"""py_rotate_square  (問題文: py_rotate_square.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def rotate_square(matrix: list[list[int]]) -> list[list[int]]:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', rotate_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
    check('1x1', rotate_square([[1]]), [[1]])
    check('2x2', rotate_square([[1, 2], [3, 4]]), [[3, 1], [4, 2]])
    check('4x4', rotate_square([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]), [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])
