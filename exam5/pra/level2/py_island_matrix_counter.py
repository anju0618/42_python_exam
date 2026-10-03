def island_matrix_counter(matrix: list[list[str]]) -> int:


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check(
        "one island",
        island_matrix_counter(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "1", "0", "0"],
                ["1", "1", "1", "1", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        ),
        1,
    )
    check(
        "three islands",
        island_matrix_counter(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        ),
        3,
    )
    check("empty matrix", island_matrix_counter([]), 0)
