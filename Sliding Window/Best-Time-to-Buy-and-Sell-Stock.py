# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l, r = 0, 1 # left=buy, right=sell
#         maxP = 0
        
#         while r < len(prices):
#             # profitable?
#             if prices[l] < prices[r]:
#                 profit = prices[r] - prices[l]
#                 maxP = max(maxP, profit)
#             else:
#                 l = r
#             r += 1
            
#         return maxP      
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0 
        
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res