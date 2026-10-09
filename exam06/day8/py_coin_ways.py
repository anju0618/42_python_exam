"""py_coin_ways  (問題文: py_coin_ways.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def coin_ways(amount: int, coins: list[int]) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', coin_ways(5, [1, 2, 5]), 4)
    check('example 2', coin_ways(3, [2]), 0)
    check('example 3', coin_ways(10, [10]), 1)
    check('amount 0', coin_ways(0, [7]), 1)
    check('no coins', coin_ways(5, []), 0)
    check('1,2,3', coin_ways(4, [1, 2, 3]), 4)
    check('one way', coin_ways(7, [2, 3]), 1)
    check('order must not matter', coin_ways(3, [1, 2]), 2)
