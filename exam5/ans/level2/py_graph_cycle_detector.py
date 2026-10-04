def py_graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    visiting = {}

    def dfs(node: int) -> bool:
        if node in visiting:
            return True
        visiting[node] = True
        for n in graph.get(node, []):
            if dfs(n):
                return True
        del visiting[node]
        return False

    for node in graph:
        if dfs(node):
            return True
    return False
