def island_matrix_counter(matrix: list[list[str]]) -> int:


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('one island', island_matrix_counter([['1', '1', '1', '1', '0'], ['1', '1', '1', '0', '0'], ['1', '1', '1', '1', '0'], ['0', '0', '0', '0', '0']]), 1)
    check('three islands', island_matrix_counter([['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]), 3)
    check('empty matrix', island_matrix_counter([]), 0)
    check('single land', island_matrix_counter([['1']]), 1)
    check('single water', island_matrix_counter([['0']]), 0)
    check('all water', island_matrix_counter([['0', '0'], ['0', '0']]), 0)
    check('all land', island_matrix_counter([['1', '1'], ['1', '1']]), 1)
    check('diagonal is not connected', island_matrix_counter([['1', '0'], ['0', '1']]), 2)
    check('checkerboard 3x3', island_matrix_counter([['1', '0', '1'], ['0', '1', '0'], ['1', '0', '1']]), 5)
    check('one row', island_matrix_counter([['1', '0', '1', '1', '0', '1']]), 3)
    check('one column', island_matrix_counter([['1'], ['1'], ['0'], ['1']]), 2)
    check('ring with lake', island_matrix_counter([['1', '1', '1'], ['1', '0', '1'], ['1', '1', '1']]), 1)
    check('ring + island in lake', island_matrix_counter([['1', '1', '1', '1', '1'], ['1', '0', '0', '0', '1'], ['1', '0', '1', '0', '1'], ['1', '0', '0', '0', '1'], ['1', '1', '1', '1', '1']]), 2)
    check('U shape (needs up move)', island_matrix_counter([['1', '0', '1'], ['1', '0', '1'], ['1', '1', '1']]), 1)
    check('snake (needs left move)', island_matrix_counter([['1', '1', '1'], ['0', '0', '1'], ['1', '1', '1'], ['1', '0', '0'], ['1', '1', '1']]), 1)
    check('corners only', island_matrix_counter([['1', '0', '0', '1'], ['0', '0', '0', '0'], ['1', '0', '0', '1']]), 4)
    check('vertical stripes', island_matrix_counter([['1', '0', '1', '0', '1'], ['1', '0', '1', '0', '1']]), 3)
