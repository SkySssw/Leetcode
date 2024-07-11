class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
    
        dict_nums1 = {}
        dict_nums2 = {}
        
        for num in nums1:
            if num not in dict_nums1:
                dict_nums1[num] = 1
            else:
                dict_nums1[num] +=1
                
        for num in nums2:
            if num not in dict_nums2:
                dict_nums2[num] = 1
            else:
                dict_nums2[num] +=1
        
        res = []
        for num in dict_nums1:
            
            if num in dict_nums2:
                inter_num = min(dict_nums1[num], dict_nums2[num])
                res.extend([num]*inter_num)
        return res