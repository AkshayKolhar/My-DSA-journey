class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        pro=0
        for i in prices[1:]:
            cost=i-mini
            pro=max(pro,cost)
            mini=min(mini,i)
        return pro