class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        for i in range(0,len(nums),2):
            min_val = min(nums[i],nums[i+1])
            max_sum += min_val
        
        return max_sum