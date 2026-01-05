class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        n = len(matrix)
        count = 0
        minv = abs(matrix[0][0])
        for i in range(n):
            for j in range(n):
                if matrix[i][j]<0:
                    count +=1
                minv = min(minv ,abs(matrix[i][j]) )
                ans += abs(matrix[i][j])


        count = count%2
        if count:
            ans = ans - minv -minv 
            
        return ans