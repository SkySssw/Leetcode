class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        str_s_dic={}
        str_t_dic={}
        
        
        for i in range(len(s)):
            str_s = s[i]
            str_t = t[i]
    
            
            
            if str_s not in str_s_dic and str_t not in str_t_dic:
                str_s_dic[str_s] = str_t
                str_t_dic[str_t] = str_s
            elif str_s_dic.get(str_s) != str_t or str_t_dic.get(str_t) != str_s:
                return False
        
        return True
                