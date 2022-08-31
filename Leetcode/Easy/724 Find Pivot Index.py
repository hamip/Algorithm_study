class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        all = sum(nums)
        
        for idx, v in enumerate(nums):
            if left == all - v - left:
                return idx
            left += v
            
        return -1 
