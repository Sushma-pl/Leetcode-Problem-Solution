class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last = 0
        c = 0
        for n in arr:
            if n-last > 1:
                temp = n-last-1
                if c+temp >= k:
                    return last+(k-c)
                c += temp
            
            last = n
        return last + (k-c)

