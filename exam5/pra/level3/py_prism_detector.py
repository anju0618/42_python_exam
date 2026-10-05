def prism_detector(grid: list[str], pattern: str):


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example', prism_detector(['CAT', 'A..', 'T..'], 'CAT'), [(0, 0, 'H'), (0, 0, 'V')])
    check('empty grid', prism_detector([], 'CAT'), [])
    check('empty pattern', prism_detector(['CAT'], ''), [])
    check('not found', prism_detector(['ABC', 'DEF'], 'XYZ'), [])
    check('H only', prism_detector(['CAT', '...'], 'CAT'), [(0, 0, 'H')])
    check('H- (right to left)', prism_detector(['TAC'], 'CAT'), [(2, 0, 'H-')])
    check('V only', prism_detector(['C', 'A', 'T'], 'CAT'), [(0, 0, 'V')])
    check('V- (bottom to top)', prism_detector(['T', 'A', 'C'], 'CAT'), [(0, 2, 'V-')])
    check('D1 (down-right)', prism_detector(['C..', '.A.', '..T'], 'CAT'), [(0, 0, 'D1')])
    check('D1- (up-left)', prism_detector(['T..', '.A.', '..C'], 'CAT'), [(2, 2, 'D1-')])
    check('D2 vector (-1, 1)', prism_detector(['..C', '.A.', 'T..'], 'CAT'), [(2, 0, 'D2')])
    check('D2- vector (1, -1)', prism_detector(['..T', '.A.', 'C..'], 'CAT'), [(0, 2, 'D2-')])
    check('pattern longer than grid', prism_detector(['CA'], 'CAT'), [])
    check('two matches in one row', prism_detector(['CATCAT'], 'CAT'), [(0, 0, 'H'), (3, 0, 'H')])
    check('palindrome both ways', prism_detector(['ABA'], 'ABA'), [(0, 0, 'H'), (2, 0, 'H-')])
    check('start not at (0,0)', prism_detector(['....', '.CAT', '....'], 'CAT'), [(1, 1, 'H')])
    check('single char matches all 8 directions', prism_detector(['A'], 'A'), [(0, 0, 'H'), (0, 0, 'H-'), (0, 0, 'V'), (0, 0, 'V-'), (0, 0, 'D1'), (0, 0, 'D1-'), (0, 0, 'D2'), (0, 0, 'D2-')])
    check('two chars 2x2', prism_detector(['AB', 'BA'], 'AB'), [(0, 0, 'H'), (0, 0, 'V'), (1, 1, 'H-'), (1, 1, 'V-')])
