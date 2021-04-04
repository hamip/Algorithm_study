'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock/'''

'''121. Best Time to Buy and Sell Stock'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 # profit always needs to be bigger than zero
        min_price = sys.maxsize # to be switched for any value to be stored
        
        for price in prices:
            # comparison of current price and minimum price so far
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit
      
