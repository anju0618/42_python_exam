def prism_detector(grid: list[str], pattern: str):


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check(
        "horizontal and vertical match",
        prism_detector(["CAT", "A..", "T.."], "CAT"),
        [(0, 0, "H"), (0, 0, "V")],
    )
    check("empty grid", prism_detector([], "CAT"), [])
