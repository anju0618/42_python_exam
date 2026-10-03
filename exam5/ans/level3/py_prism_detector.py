DIRECTIONS = [
    (1, 0, "H"),
    (-1, 0, "H-"),
    (0, 1, "V"),
    (0, -1, "V-"),
    (1, 1, "D1"),
    (-1, -1, "D1-"),
    (-1, 1, "D2"),
    (1, -1, "D2-"),
]


def prism_detector(grid: list[str], pattern: str):
    if not grid or not pattern:
        return []

    rows = len(grid)
    cols = len(grid[0])
    plen = len(pattern)
    result = []

    for y in range(rows):
        for x in range(cols):
            for dx, dy, code in DIRECTIONS:
                match = True
                for i in range(plen):
                    nx = x + dx * i
                    ny = y + dy * i
                    if ny < 0 or ny >= rows or nx < 0 or nx >= cols:
                        match = False
                        break
                    if grid[ny][nx] != pattern[i]:
                        match = False
                        break
                if match:
                    result.append((x, y, code))

    return result
