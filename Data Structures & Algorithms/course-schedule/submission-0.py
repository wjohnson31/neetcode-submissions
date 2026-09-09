class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req = defaultdict(list)
        for c, p in prerequisites:
            pre_req[c].append(p)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            
            if not pre_req[crs]:
                return True
            visited.add(crs)
            for pre in pre_req[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            pre_req[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True