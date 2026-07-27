class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set() # currently checking
        visited = set() # confirmed no cycle, course can start
        adj = defaultdict(list) # course -> [needed,...]

        for cur, pre in prerequisites:
            adj[cur].append(pre)

        def dfs(cur):
            if cur in visited:
                return True
            if cur in visiting:
                return False

            visiting.add(cur)

            for pre in adj[cur]:
                if not dfs(pre):
                    return False
            visiting.remove(cur)
            visited.add(cur)
            return True


        for cur in range(numCourses):
            if not dfs(cur):
                return False
        return True