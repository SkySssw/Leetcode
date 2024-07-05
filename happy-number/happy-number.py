class Solution:
    def isHappy(self, n: int) -> bool:
        
        sum_tot = n
        seen = set()
        
        while sum_tot != 1:
            if sum_tot in seen:
                return False
            seen.add(sum_tot)
            
            num = str(sum_tot)
            sum_tot = 0
            for n in num:
                sum_tot += int(n) ** 2
        
        return True
            
            