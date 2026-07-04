class Solution(object):
    def maxProfit(self, prices):
        min=float('inf')
        max=0
        
        for price in prices:
            if price<min:
                min=price
            elif price - min > max:
                max=price-min
        return max