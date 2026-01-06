class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def solve(d):
            ans = 0
            for n in nums:
                ans += n//d + (1 if n%d>0 else 0)
            
            return ans
        
        l, r = 1, 10**6
        while l <= r:
            m = (l+r)//2

# we want this case but ans should be as less as possible, since solve(d) < threshold which mean we can increase solve(d) which mean we should decrease the divisor/ans
            if solve(m) <= threshold:
                ans = m
                r = m-1
            else:
                l = m+1
        return ans 


