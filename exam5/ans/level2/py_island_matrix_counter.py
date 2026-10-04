def island_matrix_counter(matrix: list[list[str]]) -> int:
    count = 0

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
            return
        if matrix[r][c] != "1":
            return
        matrix[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == "1":
                count += 1
                dfs(r, c)
    return count
