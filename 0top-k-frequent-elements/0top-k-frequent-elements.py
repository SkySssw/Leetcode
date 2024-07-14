class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
       
        res = []
        
            
        sort_nums_counter = {key: val for key, val in sorted(nums_counter.items(), key = lambda ele: ele[1],reverse= True)}
        print(sort_nums_counter)
        
        for key in sort_nums_counter.keys():
            res.append(key)
        return res[:k]
       
        
