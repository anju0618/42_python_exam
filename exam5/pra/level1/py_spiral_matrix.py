def generate_spiral(n: int) -> list[list[int]]:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("3x3 spiral", generate_spiral(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
    check("1x1 spiral", generate_spiral(1), [[1]])
