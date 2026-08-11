class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_part(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

            return arr

        ind=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        if ind == -1:
            reverse_part(nums, 0, len(nums) - 1)
            return 
    
        for i in range(len(nums)-1,ind,-1):
            if nums[i]>nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
                break
        
        reverse_part(nums,ind+1,len(nums)-1)


