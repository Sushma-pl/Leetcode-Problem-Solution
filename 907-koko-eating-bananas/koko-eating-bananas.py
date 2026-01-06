class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxs = max(piles)
        def solve(s):
            t = 0
            for p in piles:
                t += p//s +(1 if p%s>0 else 0)
            return t

        l, r = 1, maxs
        ans = maxs
        while l <= r:
            m = (l+r)//2

            temp = solve(m)
            if temp <= h:
                ans = m
                r = m-1
            else:
                l = m+1
        
        return ans 
