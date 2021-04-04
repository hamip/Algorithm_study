# https://leetcode.com/problems/richest-customer-wealth/

# 1672. Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for person in accounts:
          # swap max_wealth if current sum is bigger
            if max_wealth < sum(person):
                max_wealth = sum(person)
        
        return max_wealth
    
    # Pythonic one-liner
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
     
