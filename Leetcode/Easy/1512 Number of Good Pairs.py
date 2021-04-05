# https://leetcode.com/problems/number-of-good-pairs/submissions/

# 1512. Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        
        total = 0
        # the number of pairs that can be made from n elements
        for count in counter.values():
            total += count * (count - 1) // 2
            
        return total
