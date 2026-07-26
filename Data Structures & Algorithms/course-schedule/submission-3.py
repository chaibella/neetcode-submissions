class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj, visiting, visited = defaultdict(list), set(), set()

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        def dfs(node):
            if node in visiting:
                return False # cycle detected
            if node in visited:
                return True # already confirmed valid
            
            visiting.add(node)
            for needed in adj[node]:
                if not dfs(needed):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True