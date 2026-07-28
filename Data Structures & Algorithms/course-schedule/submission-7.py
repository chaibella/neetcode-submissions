class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set() # currently checking
        visited = set() # already checked to have no cycles
        adj = defaultdict(list) # course -> [prerequisites...]

        # fill adj list first
        for cur, pre in prerequisites:
            adj[cur].append(pre)

        # setup dfs function
        def dfs(node):
            if node in visiting:
                return False # cycle detected
            if node in visited:
                return True # already verified no cycles
            
            visiting.add(node)

            for needed in adj[node]:
                if not dfs(needed):
                    return False # cycle detected within prerequisites

            visiting.remove(node)
            visited.add(node)
            return True

        # go through each course
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True