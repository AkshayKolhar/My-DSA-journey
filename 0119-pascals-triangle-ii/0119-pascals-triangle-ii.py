class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[1]
        fact=1
        for i in range(1,rowIndex+1):
            n=rowIndex-i+1
            fact=fact*n//i
            result.append(fact)

        return result