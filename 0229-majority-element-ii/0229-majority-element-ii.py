class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        comp=len(nums)//3
        result={}
        for i in nums:
            if i in result:
                result[i]+=1
            else:
                result[i]=1

        final=[]
        for i in result.keys():
            if result[i]>comp:
                final.append(i)

        return final 
