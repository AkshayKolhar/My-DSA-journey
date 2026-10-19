class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        arr=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                arr.append(i)

        return arr