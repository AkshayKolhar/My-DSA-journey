class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i,j=0,len(numbers)-1
        for num in range(len(numbers)):
            tot=numbers[i]+numbers[j]
            if tot==target:
                return [i+1,j+1]
            elif tot<target:
                i+=1
            else:
                j-=1
        

