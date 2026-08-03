class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el=-1
        c=0
        for i in nums:
            if c==0:
                c=1
                el=i
            elif i==el:
                c+=1
            else:
                c-=1
        n=0
        for i in nums:
            if i==el:
                n+=1
        if n>len(nums)//2:
            return el