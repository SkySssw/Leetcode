class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_dict = {}
        min_sum = float('inf')
        for word in list1:
            if (word in list1) and (word in list2):
                sum_ind = list1.index(word) + list2.index(word)
                common_dict[word] = sum_ind
                if sum_ind < min_sum:
                    min_sum = sum_ind

        return [word for word in common_dict if common_dict[word] == min_sum ]
        
            
                