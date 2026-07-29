class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list) # pre -> [courses]
        indegrees = defaultdict(int) # course -> numNeeded
        q = deque() # courses with indegree==0, available to start
        completed = 0 # track number of courses completed

        # setup adj and indegrees
        for cur, pre in prerequisites:
            adj[pre].append(cur)
            indegrees[cur] += 1

        # setup queue with available courses
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)

        # process available courses until queue empty
        while q:
            pre = q.popleft()
            completed += 1
            for course in adj[pre]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    q.append(course)

        # check if completed courses equal numCourses
        return completed == numCourses

