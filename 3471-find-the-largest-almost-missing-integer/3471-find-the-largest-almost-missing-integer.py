class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counts={}
        n=len(nums)
        for i in nums:
            l=0
            r=k-1
            count=0
            while l<=n-k :
                if i in nums[l:r+1]:
                    count+=1
                l+=1
                r+=1

            counts[i]=count
        ans=-1
        for i in counts.keys():
            if counts[i]==1:
                ans=max(ans,i)


        return ans
