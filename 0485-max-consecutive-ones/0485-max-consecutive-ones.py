class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        con,j=0,0
        for i in nums:
            

            if i==1:
                j+=1

            else :
                con=max(con,j)
                j=0
        con=max(con,j)
        return con