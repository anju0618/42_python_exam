def compress(s: str) -> str:


def decompress(s: str) -> str:


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('compress basic', compress('aabcccccaaa'), 'a2bc5a3')
    check('decompress basic', decompress('a2bc5a3'), 'aabcccccaaa')
    check('compress empty', compress(''), '')
    check('decompress empty', decompress(''), '')
    check('compress single char', compress('a'), 'a')
    check('compress two same', compress('aa'), 'a2')
    check('compress no repeats', compress('abc'), 'abc')
    check('compress all same', compress('aaaaa'), 'a5')
    check('compress repeat at end', compress('abbb'), 'ab3')
    check('compress repeat at start', compress('aaab'), 'a3b')
    check('compress alternating', compress('ababab'), 'ababab')
    check('compress same char split', compress('aabaa'), 'a2ba2')
    check('compress 10 chars (2 digits)', compress('aaaaaaaaaa'), 'a10')
    check('compress 12 chars + b', compress('aaaaaaaaaaaab'), 'a12b')
    check('compress uppercase/lowercase', compress('AAaa'), 'A2a2')
    check('compress spaces', compress('a  b'), 'a 2b')
    check('decompress single char', decompress('a'), 'a')
    check('decompress no counts', decompress('abc'), 'abc')
    check('decompress multi-digit', decompress('a12'), 'aaaaaaaaaaaa')
    check('decompress multi-digit + more', decompress('a12b3c'), 'aaaaaaaaaaaabbbc')
    check('decompress count 10', decompress('x10'), 'xxxxxxxxxx')
    check('decompress count 1 written', decompress('a1b1'), 'ab')
    check('decompress mixed', decompress('ab2c3d'), 'abbcccd')
    check('round trip 1', decompress(compress('aabbbccccd')), 'aabbbccccd')
    check('round trip 2', decompress(compress('zzzzzzzzzzzzy')), 'zzzzzzzzzzzzy')
