class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minp = 1
        maxp = 1

        for num in nums:
            temp = num * maxp
            maxp, minp = max(num, minp * num, maxp * num), min(num, minp * num, num * maxp)
            res = max(res, maxp)
        
        return res