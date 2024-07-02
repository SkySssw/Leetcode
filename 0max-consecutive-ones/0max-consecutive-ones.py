class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zero_ind = [ind for ind in range(len(nums)) if nums[ind] == 0]
        
        if len(zero_ind) == 1:
            return max(len(nums)-1 - zero_ind[0],zero_ind[0])
        elif len(zero_ind) == 0:
            return len(nums)
        
        max_gap = 0
        for i in range(len(zero_ind)-1):
            diff = zero_ind[i+1] - zero_ind[i] -1
            if diff > max_gap:
                max_gap = diff
                
        max_gap = max(max_gap, zero_ind[0], len(nums) - 1 - zero_ind[-1])
        return max_gap 
                