class Solution:
    def hammingWeight(self, n: int) -> int:
        numbits = 0
        while n:
            numbits += n & 1
            n >>= 1
        return numbits