class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        for i in range(len(s)):
            if len(s)==len(goal) and goal in s+s:
                return True
            return False

            

        
