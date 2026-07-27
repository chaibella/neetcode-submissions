class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list) # prereq -> [course,...]
        indegrees = defaultdict(int) # course -> numCoursesNeeded
        q = deque() # courses available to take now
        completed = 0

        for cur, pre in prerequisites:
            adj[pre].append(cur)
            indegrees[cur] += 1
        
        for cur in range(numCourses):
            if indegrees[cur] == 0:
                q.append(cur)

        while q:
            pre = q.popleft()
            completed += 1
            for course in adj[pre]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    q.append(course)

        return completed == numCourses