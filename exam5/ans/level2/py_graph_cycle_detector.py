def py_graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    if not graph:
        return False

    state = {}

    def dfs(node: int) -> bool:
        if state.get(node) == "visiting":
            return True
        if state.get(node) == "done":
            return False

        state[node] = "visiting"
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True
        state[node] = "done"
        return False

    for node in graph:
        if node not in state and dfs(node):
            return True
    return False
