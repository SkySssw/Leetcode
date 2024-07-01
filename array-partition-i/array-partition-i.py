class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_list=[]
        for i in range(0,len(nums),2):
            min_val = min(nums[i],nums[i+1])
            min_list.append(min_val)
        
        return sum(min_list)