class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i in nums:
            if i>=0:
                p.append(i)
            else:
                n.append(i)
        i,j=0,0
        for k in range(len(nums)):
            if k%2==0:
                nums[k]=p[i]
                i+=1
            else:
                nums[k]=n[j]
                j+=1
        return nums