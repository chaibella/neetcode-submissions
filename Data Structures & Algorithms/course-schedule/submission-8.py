class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list) # prerequisite -> [courses...]
        indegrees = defaultdict(int) # course -> numPrerequisites
        q = deque() # courses available to take now, indegree is 0
        completed = 0 # courses successfully completed (started)

        # setup adj list and update indegrees
        for cur, pre in prerequisites:
            adj[pre].append(cur)
            indegrees[cur] += 1

        # start queue with available courses
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)

        # continue processing until no more available courses
        while q:
            pre = q.popleft()
            completed += 1
            for course in adj[pre]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    q.append(course)

        # if processed courses matching numCourses, we've completed all course
        return completed == numCourses