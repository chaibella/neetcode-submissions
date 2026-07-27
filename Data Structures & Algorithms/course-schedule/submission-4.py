class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set() # verified no cycle
        visiting = set() # currently checking
        adj = defaultdict(list) # course -> [needed,...]

        for course, needed in prerequisites:
            adj[course].append(needed) # add the mapping

        def dfs(node):
            if node in visited:
                return True # already confirmed no cycle
            if node in visiting:
                return False # currently checking, so seeing again means cycle

            visiting.add(node) # mark current course as visiting
            for needed in adj[node]:
                if not dfs(needed): # if required course couldnt start/has cycles
                    return False
            visiting.remove(node) # otherwise, all reqs satisfied without cycle
            visited.add(node) # and course can start
            return True

        for course in range(numCourses):
            if not dfs(course): # if any course has cycle in its prereqs
                return False        # then we can't start it
        return True # all courses could be taken, no cycles in reqs