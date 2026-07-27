class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for l in edges:
            adj[l[0]].append(l[1])
            adj[l[1]].append(l[0])
        
        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for n in adj[node]:
                if n == parent:
                    continue
                if n in visited:
                    return False
                if not dfs(n, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n

