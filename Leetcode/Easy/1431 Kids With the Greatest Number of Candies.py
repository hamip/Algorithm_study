# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for kid in candies:
            if kid + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
                
        return result
    
    # One-liner can do (list comprehension)
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]: 
        return [candy+extraCandies >= max(candies) for candy in candies]
      
      
