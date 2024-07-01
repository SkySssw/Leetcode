class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lPtr = 0
        rPtr = len(numbers)-1
        
        while lPtr < rPtr:
            result = numbers[lPtr]+numbers[rPtr]
            if result ==  target:
                return [lPtr+1, rPtr+1]
            elif result > target:
                rPtr -= 1
            else :
                lPtr += 1