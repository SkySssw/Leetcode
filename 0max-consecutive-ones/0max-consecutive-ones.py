class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0 
       
        max_gap = 0
        
        for num in nums:
            if num == 1:
                counter +=1
                
            else:
                max_gap = max(counter, max_gap)
                counter = 0
        
        max_gap = max(counter,max_gap)
                
        return max_gap 
                