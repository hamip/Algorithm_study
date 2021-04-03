'''https://leetcode.com/problems/product-of-array-except-self/'''

'''238. Product of Array Except Self'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product cannot be initialized as zero
        product = 1
        result = []
        
        # product of left side
        for i in range(len(nums)):
            result.append(product)
            product = product * nums[i]
        
        product = 1
        # multiply the right side values to the left side product
        for i in range(len(nums)-1,-1,-1):
            result[i] = result[i] * product
            product = product * nums[i]
            
        return result
      
