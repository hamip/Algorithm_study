# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

# 1281. Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total = 0
        product = 1
        for x in str(n):
            total += int(x)
            product *= int(x)
            
        return product - total
