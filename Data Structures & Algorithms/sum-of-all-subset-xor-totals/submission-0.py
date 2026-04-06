class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = [[]]
        total = 0
        
        for num in nums:
            cp = [s.copy() for s in subsets]
            for s in cp:
                s.append(num)
                xorsum = 0
                for i in s:
                    xorsum ^= i
                total += xorsum
            subsets += cp

        print(subsets)

        return total 