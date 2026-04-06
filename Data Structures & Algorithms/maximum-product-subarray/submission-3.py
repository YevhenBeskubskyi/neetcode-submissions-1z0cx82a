class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minp = 1
        maxp = 1

        for num in nums:
            temp = num * maxp
            maxp = max(num, maxp * num, minp * num)
            minp = min(temp, minp * num, num)
            res = max(res, maxp)
        
        return res