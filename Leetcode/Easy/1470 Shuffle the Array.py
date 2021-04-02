'''ttps://leetcode.com/problems/shuffle-the-array/'''

'''1470. Shuffle the Array'''

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #list length is always 2 * n
        first_half = nums[:n]
        last_half = nums[n:]
        res = []
        
        for i in range(n):
            res.append(first_half[i])
            res.append(last_half[i])
            
        return res
      
