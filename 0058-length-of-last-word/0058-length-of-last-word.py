class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w=s.split()
        return len(w[-1])

        