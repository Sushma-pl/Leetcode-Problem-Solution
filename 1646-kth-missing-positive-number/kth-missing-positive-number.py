class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        total = arr[n-1]-n
        if k > total:
            return arr[n-1]+(k-total)
        
        l, r = 0, n-1
        ind = -1
        while l <= r:
            m = (l+r)//2
            missing = arr[m]-(m+1)

            if k > missing:
                l = m+1
            elif k <= missing:
                ind = m
                r =m-1
        
        # at l , total missing , we have reduce the value at l by tm-k+1
        tm = arr[l]-(l+1)
        ans = arr[l] - (tm-k+1)
        return ans 
                
        
