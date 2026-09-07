def word_ladder(start: str, end: str, sentence: list[str]) -> int:
    # TODO: implement without collections.deque
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check(
        "ladder exists",
        word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
        5,
    )
    check(
        "no ladder",
        word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),
        0,
    )
