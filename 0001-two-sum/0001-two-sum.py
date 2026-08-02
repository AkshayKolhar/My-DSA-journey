class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            n=nums[i]
            m=target-n
            if m in h:
                return [h[m],i]
            
            h[n]=i
            

        