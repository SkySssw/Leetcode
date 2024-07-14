
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_counter = Counter(stones)
        
        res = 0
        for j in jewels:
            res += stones_counter[j]
        
        return res
        
        