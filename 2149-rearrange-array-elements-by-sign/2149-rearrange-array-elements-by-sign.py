class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        a,b=0,1
        for i in nums:
            if i>=0:
                arr[a]=i
                a+=2
            else:
                arr[b]=i
                b+=2


        
        return arr