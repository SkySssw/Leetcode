class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        
        
        longest_subs = 0
        left = 0
        char_index_map={}
        for right, c in enumerate(s):
            if c in char_index_map and char_index_map[c] >= left:
                left = char_index_map[c] + 1
            char_index_map[c] = right
            longest_subs = max(longest_subs, right-left+1)
        
        return longest_subs