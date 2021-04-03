'''https://leetcode.com/problems/trapping-rain-water/'''

'''42. Trapping Rain Water'''

class Solution:
    def trap(self, height: List[int]) -> int:
        #if height does not have elements
        if not height:
            return 0

        water_volume = 0
        left, right = 0, len(height) - 1
        left_bar, right_bar = height[left], height[right]

        while left < right:
            # choose the higher bar to opereate subtraction later
            left_bar, right_bar = max(height[left], left_bar), max(height[right], right_bar)
            
            # move the pointer to higher bar
            if left_bar <= right_bar:
                water_volume += left_bar - height[left]
                left += 1
            else:
                water_volume += right_bar - height[right]
                right -= 1
                
        return water_volume
