class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort() 
        discounts.sort() 
        total = sum(prices) 
        for i in range(min(len(prices), len(discounts))): 
            price = prices[-1 - i] 
            discount = discounts[-1 - i] 
            total -= price * discount / 100 
        return total