class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1

        def solve(d):
            b = 0
            continuosday = 0
            for n in bloomDay:
                if d>=n:
                   continuosday +=1
                else:
                    continuosday= 0
                
                if continuosday == k:
                    b += 1
                    continuosday = 0
            
            return b
        
        l ,r = min(bloomDay), max(bloomDay)
        ans = -1
        while l <= r:
            d = (l+r)//2
            temp = solve(d)

            if temp >= m:
                ans = d
                r = d-1
            else:
                l = d+1

        return ans 
