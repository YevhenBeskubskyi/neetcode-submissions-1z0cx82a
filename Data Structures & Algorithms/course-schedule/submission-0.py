class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for c, p in prerequisites:
            adj[p].append(c)
            indegree[c] += 1
        
        queue = deque([c for c, p in enumerate(indegree) if p == 0])
        count = 0

        while queue:
            course = queue.popleft()
            count += 1

            neighbors = adj[course]
            for neighbor in neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            
        return count == numCourses