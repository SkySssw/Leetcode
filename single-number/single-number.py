class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        single_num = 0
        
        for num in nums:
            single_num ^= num
        return single_num
    
#     class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
        
#         temp_set = set()
#         dup_list = []
        
#         for num in nums:
#             if num not in temp_set:
#                 temp_set.add(num)
#             else:
#                 dup_list.append(num)
        
#         for num in nums:
#             if num not in dup_list:
#                 return num
            