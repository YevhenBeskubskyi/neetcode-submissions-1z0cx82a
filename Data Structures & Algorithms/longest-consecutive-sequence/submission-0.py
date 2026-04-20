class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)

        for num in nums:
            diff = 0
            while num - diff in numset:
                diff += 1
            longest = max(longest, diff)
        
        return longest