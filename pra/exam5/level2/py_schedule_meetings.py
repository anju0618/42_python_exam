def schedule_meetings(intervals: list[tuple[int, int]]) -> tuple[int, list]:
    # TODO: implement without sorted()/.sort()
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check(
        "three meetings, two rooms",
        schedule_meetings([(0, 30), (5, 10), (15, 20)]),
        (2, [[(0, 30)], [(5, 10), (15, 20)]]),
    )
    check("empty list", schedule_meetings([]), (0, []))
