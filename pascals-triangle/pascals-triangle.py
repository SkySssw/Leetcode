class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for n in range(numRows):
            row = [1] * (n+1)
            
            for j in range(1,n):
                row[j] =  pascal[n-1][j-1] + pascal[n-1][j]
            
            pascal.append(row)
        return pascal