class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        con=0
        for i in nums:
            lenght=len(str(i))
            if lenght%2==0:
                con+=1
        return con