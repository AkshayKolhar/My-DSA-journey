class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i,j=0,0
        while j<len(nums):
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
            j+=1
        for n in range(i,j):
            nums[n]=0
