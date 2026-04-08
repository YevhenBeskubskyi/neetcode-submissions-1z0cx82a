class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()

        for i, n in enumerate(nums):
            if n in diff:
                return [diff[n], i]
            diff[target-n] = i