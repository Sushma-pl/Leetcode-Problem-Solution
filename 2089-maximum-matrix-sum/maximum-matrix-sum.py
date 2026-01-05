class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        n = len(matrix)
        count = 0
        arr = []
        for i in range(n):
            for j in range(n):
                ans += matrix[i][j]
                if matrix[i][j]<0:
                    count +=1
                arr.append(abs(matrix[i][j]))

        count = count%2
        arr.sort()
        # print(arr)
        # print(count)
        ans = sum(arr[count:])-sum(arr[:count])
        return ans