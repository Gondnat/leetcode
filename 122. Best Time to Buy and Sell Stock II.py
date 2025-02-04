from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4])) # 7
    print(s.maxProfit([1,2,3,4,5])) # 4
    print(s.maxProfit([7,6,4,3,1])) # 0
    print(s.maxProfit([1,2,3,4,5,6,7])) # 6
    print(s.maxProfit([1,2,3,4,5,6,7,1,2,3,4,5,6,7])) # 12
    print(s.maxProfit([1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7])) # 18
    print(s.maxProfit([1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7])) # 24