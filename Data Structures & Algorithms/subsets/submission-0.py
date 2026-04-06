class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            cp = [s.copy() for s in res]
            for s in cp:
                s.append(num)
            res += cp

        return res