class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        rPtr = len(s) - 1
        lPtr = 0
        
        while (rPtr>lPtr):
            s[lPtr], s[rPtr] = s[rPtr], s[lPtr]
            
            rPtr -= 1
            lPtr += 1
       