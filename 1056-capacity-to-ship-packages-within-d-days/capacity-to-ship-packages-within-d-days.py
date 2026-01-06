class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        def solve(capacity):
            s = 0
            d = 0
            for w in weights:
                if s+w > capacity:
                    d += 1
                    s = w
                else:
                    s+= w
            
            if s > 0:
                d+=1

            return d
        
        l, r = max(weights), sum(weights)
        ans = sum(weights)
        while l <= r:
            c = (l+r)//2

            temp = solve(c)
            if temp <= days:
                r = c-1
                ans = c
            else:
                l = c+1
        
        return ans 