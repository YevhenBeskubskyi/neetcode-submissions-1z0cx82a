class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c1, c2 = cost[0], cost[1]
        
        for c in cost[2:]:
            print(c1, c2)
            c1, c2 = c2, min(c1 + c, c2 + c)
        
        print(c1, c2)
        return min(c1, c2)