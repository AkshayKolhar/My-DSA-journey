class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        return max(h,key=h.get)