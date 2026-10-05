def word_ladder(start: str, end: str, sentence: list[str]) -> int:


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', word_ladder('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']), 5)
    check('example 2 (end missing)', word_ladder('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']), 0)
    check('one step', word_ladder('hot', 'dot', ['dot']), 2)
    check('single letter words', word_ladder('a', 'c', ['a', 'b', 'c']), 2)
    check('empty sentence', word_ladder('hit', 'cog', []), 0)
    check('end in list but unreachable', word_ladder('hit', 'cog', ['hot', 'cog']), 0)
    check('start not in list is fine', word_ladder('hit', 'hot', ['hot']), 2)
    check('two letters changed is not a step', word_ladder('hit', 'hog', ['hog']), 0)
    check('shortest of two paths', word_ladder('aaa', 'ccc', ['baa', 'bba', 'bbb', 'cbb', 'ccb', 'ccc', 'caa', 'cca']), 4)
    check('direct one step (extra words ignored)', word_ladder('lost', 'cost', ['most', 'fist', 'lost', 'cost', 'fish']), 2)
    check('longer chain', word_ladder('cold', 'warm', ['cord', 'card', 'ward', 'warm', 'cold', 'word', 'worm']), 5)
    check('dead end branch', word_ladder('abc', 'xyz', ['abz', 'ayz', 'xyz', 'abd']), 4)
