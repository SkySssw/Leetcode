class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        ans = -1
        
        for i in range(len(haystack)):
            if needle == haystack[i:i+len_needle]:
                return i
        return ans
        