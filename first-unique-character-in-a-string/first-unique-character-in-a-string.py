class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        res = -1
        
        for x in s:
            if x not in count:
                count[x] = 1
            else:
                count[x] +=1
        
        for i,x in enumerate(s):
            if count[x] == 1:
                return i
        
        return res