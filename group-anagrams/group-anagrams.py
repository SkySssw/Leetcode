class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strs_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in strs_dict:
                strs_dict[sorted_word]=[word]
            else :
                strs_dict[sorted_word].append(word)
        
        return strs_dict.values()