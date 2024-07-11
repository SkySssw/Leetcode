class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dup_dict = {}
        for i,num in enumerate(nums):
            if num not in dup_dict:
                dup_dict[num] = [i]
            else:
                for prev_ind in dup_dict[num]:
                    diff = abs(prev_ind - i)
                    if diff <= k:
                        return True
                dup_dict[num].append(i)
        
        return False
        
        
        