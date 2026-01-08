class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[-sys.maxsize]*(n2) for _ in range(n1)]
        def solve(i, j):
            if i >= n1 or j >= n2:
                return 0
            
            if dp[i][j]!=-sys.maxsize:
                return dp[i][j]
            
            # i am taking ans 0 , to consider emty subsequences also
            ans = 0
            t1 = nums1[i]*nums2[j] + solve(i+1, j+1)
            t2 = solve(i, j+1)
            t3 = solve(i+1, j)
            ans = max(ans,max(t1,t2,t3))
            # for i1 in range(i, n1):
            #     for j1 in range(j, n2):
            #         temp = nums1[i1]*nums2[j1]
            #         ans = max(ans, temp+solve(i1+1, j1+1))
            
            dp[i][j] =  ans 
            return ans 

        ans  = -sys.maxsize
        for i in range(n1):
            for j in range(n2):
                ans = max(ans, nums1[i]*nums2[j] + solve(i+1, j+1))

        return ans

        

