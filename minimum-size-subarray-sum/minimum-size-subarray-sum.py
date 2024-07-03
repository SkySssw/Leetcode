class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        right = 0
        min_val = float('inf')
        sumOfCurrent = 0
        
        for right in range(len(nums)):
            sumOfCurrent += nums[right]
            
            while sumOfCurrent >= target:
                sumOfCurrent -= nums[left]
                min_val = min(min_val, right - left + 1)
                left += 1
                
        return 0 if min_val == float('inf') else min_val