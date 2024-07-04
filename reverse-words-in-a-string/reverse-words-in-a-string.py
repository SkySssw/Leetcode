class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        ans_list = s_list[::-1]
        ans = " ".join(ans_list)
        #for a in ans_list[1:]:
         #   ans += " "+a
        return ans
        