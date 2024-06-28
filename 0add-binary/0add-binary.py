class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_num = int(a,2)
        b_num = int(b,2)
        
#         for n,x in enumerate(a):
#             a_num += int(x)*2**(len(a)-1-n)
            
#         for n,x in enumerate(b):
#             b_num += int(x)*2**(len(b)-1-n)
        
        sum_ab = a_num + b_num
        
        if sum_ab == 0:
            return "0"
        
        ans=[]
        while sum_ab > 0:
            remainder = sum_ab % 2
            ans += str(remainder)
            sum_ab //= 2
        ans.reverse()
        return ''.join(ans)
            