# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyPointer = 0
        sellPointer = 1
        
        while sellPointer < len(prices):
            # Is it Profit?
            if prices[buyPointer] < prices[sellPointer]:
                currentProfit = prices[sellPointer] - prices[buyPointer]
                profit = max(profit, currentProfit)
            else:
                buyPointer = sellPointer
            sellPointer += 1
            
        return profit