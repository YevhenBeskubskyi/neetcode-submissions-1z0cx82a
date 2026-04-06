class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtrack(i, candidate):
            if len(candidate) == k:
                combinations.append(list(candidate))
                return
            for j in range(i, n+1):
                candidate.append(j)
                backtrack(j + 1, candidate)
                candidate.pop()
        
        backtrack(1, [])
        return combinations
