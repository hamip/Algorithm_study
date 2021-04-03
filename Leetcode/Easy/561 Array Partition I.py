'''https://leetcode.com/problems/array-partition-i/'''

'''561. Array Partition I'''

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = [v for i, v in enumerate(nums) if i % 2 == 0]
        
        return sum(res)
