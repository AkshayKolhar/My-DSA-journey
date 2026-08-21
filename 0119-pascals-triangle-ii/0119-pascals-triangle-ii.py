class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def Ncr(n,r):
            res=1
            for i in range(r):
                res=res*(n-i)
                res=res/(i+1)

            return res


        res_row=[]
        rowIndex+=1
        for c in range(1,rowIndex+1):
            res_row.append(int(Ncr(rowIndex-1,c-1)))

        return res_row
