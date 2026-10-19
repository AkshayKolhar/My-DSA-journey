class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        arr=[]
        n=len(nums)
        for i in nums:
            if i!=0:
                arr.append(i)
                n-=1
        for i in range(n):
            arr.append(0)

        for i in range(len(nums)):
            nums[i]=arr[i]

        
        
        