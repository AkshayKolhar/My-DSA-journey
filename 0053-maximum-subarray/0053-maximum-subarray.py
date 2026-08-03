class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        m=max(nums)
        a_s=-1
        a_e=-1
        for i in nums:
            if s==0:
                start=i
                
            s+=i
            if s>m:
                m=s
                a_s,a_e=start,i
            if s<0:
                s=0

        return m