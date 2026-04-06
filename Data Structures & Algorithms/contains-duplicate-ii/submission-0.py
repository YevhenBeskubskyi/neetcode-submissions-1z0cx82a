class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_idx = dict()

        for i, num in enumerate(nums):
            if num in num_to_idx and abs(i - num_to_idx[num]) <= k:
                return True
            num_to_idx[num] = i
        
        return False