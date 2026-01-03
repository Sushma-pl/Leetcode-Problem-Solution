class Solution:
    def numOfWays(self, n: int) -> int:
        firstrow = []
        count = 0
        
        def fstate(i, op):
            if i >=3:
                firstrow.append(op)
                return 
            
            for ch in "RGY":
                if op=="" or op[-1]!=ch:
                    fstate(i+1, op+ch)
        
        fstate(0,"")
        dp = {}
        

        def isPossible(p, lastrow):
            for i in range(len(p)):
                if p[i] == lastrow[i]:
                    return False
            return True  

        def solve(row, lastrow):
            if row >= n:
                return 1 
            
            if (row, lastrow) in dp:
                return dp[(row, lastrow)]

            ans = 0
            for p in firstrow:
                if isPossible(p, lastrow):
                    ans += solve(row+1, p)
                    ans = ans % (10**9 + 7)
            
            dp[(row, lastrow)] = ans 
            return ans % (10**9 + 7)

        for p in firstrow:
            count += solve(1, p)
            count = count % (10**9 + 7)
        
        return count 
                
    
    
        return 0
