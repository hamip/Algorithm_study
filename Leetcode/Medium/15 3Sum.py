'''https://leetcode.com/problems/3sum/'''

'''15. 3Sum'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        # len(nums) - 2 because at least three elements are needed
        for i in range(len(nums) - 2):
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # two-pointer approach
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                # if sum < 0, sum needs to be bigger; shift to the right || vice versa
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else: # sum = 0
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # if same element is adjacent, skip it
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # move pointer
                    left += 1
                    right -= 1
        
        return result
      
      
