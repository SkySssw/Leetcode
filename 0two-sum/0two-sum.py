class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1st Solution
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        store_diff = {}
        for i in range(len(nums)):
            num = nums[i]
            if target-num in store_diff:
                return [i, store_diff[target-num]]
            store_diff[num] =  i