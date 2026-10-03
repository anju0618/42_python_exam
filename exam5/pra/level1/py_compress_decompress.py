def compress(s: str) -> str:
    # TODO: implement
    pass


def decompress(s: str) -> str:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("compress basic", compress("aabcccccaaa"), "a2bc5a3")
    check("decompress basic", decompress("a2bc5a3"), "aabcccccaaa")
    check("compress empty", compress(""), "")
