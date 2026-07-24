class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        path = set()
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[prereq].append(course)

        def dfs(node):
            if node in path:
                return False # cycle detected
            if node in visited:
                return True # already confirmed safe no need to re-explore
            
            path.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False # cycle found deeper in branch
            path.remove(node)
            visited.add(node)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
