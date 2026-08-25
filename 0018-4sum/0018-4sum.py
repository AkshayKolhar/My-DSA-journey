class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                seen=set()
                for k in range(j+1,n):
                    summ=nums[i]+nums[j]+nums[k]
                    fourth=target-summ
                    if fourth in seen:
                        sum_4=sorted([nums[i],nums[j],nums[k],fourth])

                        if sum_4 not in result:
                            result.append(sum_4)
                    seen.add(nums[k])

        return result