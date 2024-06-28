class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        index = 0
        for ind in range(len(nums)):
            if nums[ind] != val:
                nums[index] = nums[ind]
                index+=1
                
        k  = len(nums[:index])
        
        return k
                
      
                