class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        wrtPtr = len(s) - 1
    
        half_len_s = int(len(s)/2)
        for rdPtr in range(half_len_s):
            rdAlp = s[rdPtr]
            s[rdPtr] = s[wrtPtr]
            s[wrtPtr] = rdAlp
            
            wrtPtr -= 1