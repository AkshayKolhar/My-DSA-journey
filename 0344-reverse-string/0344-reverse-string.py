class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        f=0
        l=len(s)-1
        while f<=l:
            s[f],s[l]=s[l],s[f]
            f+=1
            l-=1

        