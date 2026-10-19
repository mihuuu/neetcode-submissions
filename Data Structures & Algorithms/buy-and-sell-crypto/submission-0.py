class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        # current i = sell value
        for i in range(1, len(prices)):
            if prices[i] > buy:
                res = max(res, prices[i] - buy)
            # update buy = current min value
            buy = min(buy, prices[i])
        
        return res