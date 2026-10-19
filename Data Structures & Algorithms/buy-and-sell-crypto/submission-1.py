class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        # current i = sell value
        for cur in prices:
            res = max(res, cur - buy)
            # update buy = current min value
            buy = min(buy, cur)
        
        return res