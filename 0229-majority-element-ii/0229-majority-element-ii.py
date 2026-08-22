class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=0
        c2=1
        cn1=0
        cn2=0

        for num in nums:
            if num==c1:
                cn1+=1
            elif num==c2:
                cn2+=1
            elif cn1==0:
                c1=num
                cn1=1
            elif cn2==0:
                c2=num
                cn2=1
            else:
                cn1-=1
                cn2-=1
            
        cn1=0
        cn2=0

        for i in nums:
            if i ==c1:
                cn1+=1
            elif i==c2:
                cn2+=1
        
        result=[]
        n=len(nums)

        if cn1>n//3:
            result.append(c1)
        if cn2>n//3:
            result.append(c2)

        return result 